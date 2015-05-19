# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from datetime import *
from models import *
usuario = Blueprint('usuario', __name__)


@usuario.route('/usuario/ADesconectarseUsuario')
def ADesconectarseUsuario():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPortada', 'msg':[ur'Usuario desconectado'], "actor":None}, ]
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
    evento = request.get_json()
    results = [{'label':'/VEventoUsuario', 'msg':[ur'Generar certificado']}, {'label':'/VEventoUsuario', 'msg':[ur'Usted no asistio a este evento']} ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    usuario = session['correo']
    reserva = dbsession.query(Reserva).get((usuario,evento))

    if reserva.asistencia:
       fecha_actual = datetime.now().__str__()
       certificado = Certificado(fecha_actual,usuario,evento)
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
    results = [{'label':'/VEventoUsuario', 'msg':[ur'Generar credencial']}, ]
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
    evento = request.args['evento']
    results = [{'label':'/VInicioUsuario', 'msg':[ur'Inscripcion OK']}, {'label':'/VEventoUsuario', 'msg':[ur'Inscripcion ERROR']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    usuario = session['correo']
    reserva = dbsession.query(Reserva).get((usuario,evento))
    
    if not reserva:
        dbsession.add( Reserva(actor_correo=usuario, evento_id=int(evento), asistencia=0) )
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



@usuario.route('/usuario/VAficheUsuario')
def VAficheUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VCertificadoUsuario')
def VCertificadoUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VEventoUsuario/<idEvento>')
def VEventoUsuario(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    print "Ejecutando VEventoUsuario"
    evento = dbsession.query(Evento).get(idEvento)
    admin = dbsession.query(Actor).get(evento.administrador)
    
    res['id'] = evento.id
    res['nombreEvento'] = evento.nombre
    res['descripcion'] = evento.descripcion
    res['fecha'] = evento.fecha
    res['lugar'] = evento.lugar
    res['nroCupos'] = evento.total_cupos
    res['cuposDisponibles'] = evento.cupos_disponibles
    res['nombreAdmin'] = admin.nombre

    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VInicioUsuario')
def VInicioUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    aux = dbsession.query(Evento).order_by(Evento.id.desc()).all()
	
    res['eventos'] = []
    for evento in aux :
        res['eventos'].append({'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles})
        
    reservas = dbsession.query(Reserva).filter(Reserva.actor_correo == session['correo'])
    
    res['eventos_inscritos'] = []    
    for r in reservas:
        e = dbsession.query(Evento).get(r.evento_id)
        res['eventos_inscritos'].append({ 'id' : e.id, 'nombre' : e.nombre, 'fecha' : e.fecha, 'lugar' : e.lugar })

    #Action code ends here
    return json.dumps(res)
 
    
@usuario.route('/usuario/VCredenciales/<idEvento>')
def VCredenciales(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    e = dbsession.query(Evento).get(idEvento)
    res = { 'id' : e.id, 'nombre' : e.nombre, 'fecha' : e.fecha, 'lugar' : e.lugar }

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
