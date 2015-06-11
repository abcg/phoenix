# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json, current_app
from datetime import *
from models import *
from dateManager import *

usuario = Blueprint('usuario', __name__)


@usuario.route('/usuario/ADesconectarseUsuario')
def ADesconectarseUsuario():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPortada', 'msg':[ur'¡Hasta pronto, %s!' % (session['usuario'])], "actor":None}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    session.pop('usuario')
    session.pop('correo')

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@usuario.route('/usuario/AGenerarCertificado')
def AGenerarCertificado():
    #GET parameter
    evento = request.args['evento']
    results = [{'label':'/VEventoUsuario', 'msg':[ur'Su certificado ha sido generado.']},
               {'label':'/VEventoUsuario', 'msg':[ur'Usted no asistió a este evento.']}
    ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    usuario = session['correo']
    reserva = dbsession.query(Reserva).get((usuario,evento))

    if reserva and reserva.asistencia:
       fecha_actual = str(datetime.now())
       certificado = Certificado(fecha_de_generacion=fecha_actual,actor_correo=usuario,evento_id=evento)
       dbsession.add(certificado)
       dbsession.commit()
    else:
       res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@usuario.route('/usuario/AGenerarCredencial')
def AGenerarCredencial():
    #GET parameter
    evento = request.args['evento']
    results = [{'label':'/VEventoUsuario', 'msg':[ur'Su credencial ha sido generada.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@usuario.route('/usuario/AInscribirEvento')
def AInscribirEvento():
    #GET parameter
    e_id = request.args['evento']
    results = [{'label':'/VInicioUsuario', 'msg':[ur'La reserva se ha realizado con éxito.']},
               {'label':'/VEventoUsuario', 'msg':[ur'Hubo un error al procesar la reserva.']},
               {'label':'/VEventoUsuario', 'msg':[ur'Reserva sin efecto. No hay cupos disponibles para este evento.']},
               {'label':'/VEventoUsuario', 'msg':[ur'Reserva sin efecto. Ud. ya había reservado un cupo para este evento.']},
              ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    usuario = session['correo']
    evento  = dbsession.query(Evento).get(e_id)
    reserva = dbsession.query(Reserva).get((usuario,e_id))
    
    if not reserva:
        if evento.cupos_disponibles > 0:
            evento.cupos_disponibles -= 1
            dbsession.add( Reserva(actor_correo=usuario, evento_id=int(e_id), asistencia=0) )
            dbsession.add(evento)
            dbsession.commit()
        else:
            res = results[2]
    else:
        res = results[3]
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@usuario.route('/usuario/VAficheUsuario/<idEvento>')
def VAficheUsuario(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    evento = dbsession.query(Evento).get(idEvento)
    res['afiche'] = evento.afiche
    res['id'] = evento.id

    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VCertificadoUsuario/<idEvento>')
def VCertificadoUsuario(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    usuario = session['correo']
    actor = dbsession.query(Actor).get(usuario)
    e = dbsession.query(Evento).get(idEvento)
    res = { 'id' : e.id, 'nombre' : e.nombre, 'descripcion' : e.descripcion, 'fecha' : e.fecha, 'lugar' : e.lugar, 'participante' : actor.nombre }

    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VEventoUsuario/<idEvento>')
def VEventoUsuario(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    evento = dbsession.query(Evento).get(idEvento)
    admin = dbsession.query(Actor).get(evento.administrador)
    reserva = dbsession.query(Reserva).get((session['correo'],idEvento))

    hoy = today()
    fecha_evento = parseDate(evento.fecha)
    
    res['id'] = evento.id
    res['nombreEvento'] = evento.nombre
    res['descripcion'] = evento.descripcion
    res['fecha'] = evento.fecha
    res['lugar'] = evento.lugar
    res['nroCupos'] = evento.total_cupos
    res['cuposDisponibles'] = evento.cupos_disponibles
    res['nombreAdmin'] = admin.nombre
    res['afiche'] = evento.afiche

    res['inscrito'] = reserva is not None
    res['asistio'] = res['inscrito'] and reserva.asistencia is 1
    res['evento_realizado'] = fecha_evento < hoy
    res['evento_cerrado'] = evento.cerrado
    res['certificado_generado'] = dbsession.query(Certificado).filter(Certificado.actor_correo==session['correo'], Certificado.evento_id==evento.id).count()

    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VInicioUsuario')
def VInicioUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    eventos = dbsession.query(Evento).order_by(Evento.id.desc()).all()
    res['eventos_no_reservados'] = []
    res['eventos_reservados'] = []    
	
    hoy = today()
    for evento in eventos :
        reserva = dbsession.query(Reserva).get((session['correo'], evento.id))
        if reserva is not None:
            res['eventos_reservados'].append({ 'id' : evento.id, 'nombre' : evento.nombre, 'fecha' : evento.fecha, 'lugar' : evento.lugar })
        else:
            if parseDate(evento.fecha) >= hoy:
                res['eventos_no_reservados'].append({'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles})
        
    #Action code ends here
    return json.dumps(res)
 
    
@usuario.route('/usuario/VCredenciales/<idEvento>')
def VCredenciales(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    e = dbsession.query(Evento).get(idEvento)
    res = { 'id' : e.id, 'nombre' : e.nombre, 'descripcion' : e.descripcion,'fecha' : e.fecha, 'lugar' : e.lugar }

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
