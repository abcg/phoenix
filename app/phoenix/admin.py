# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from datetime import *
from models import *
admin = Blueprint('admin', __name__)

def parseDate(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def today():
    return datetime.now().date()

def dateToString(date):
    date.strftime('%Y-%m-%d')

@admin.route('/admin/ADesconectarse')
def ADesconectarse():
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



@admin.route('/admin/AEliminarEvento')
def AEliminarEvento():
    #GET parameter
    evento = request.args['evento']
    results = [{'label':'/VInicioAdministrador', 'msg':[ur'Evento eliminado']}, {'label':'/VEvento', 'msg':[ur'Evento no eliminado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    print "Ejecutando rutina AEliminarEvento con parametro %s" % evento
    e = dbsession.query(Evento).get(evento)
    hoy = today()
    fecha_evento = parseDate(e.fecha)

    if fecha_evento < hoy:
        res = results[1]
    else:
        # Primero, eliminar las reservas asociadas al evento
        dbsession.query(Reserva).filter(Reserva.evento_id==evento).delete(synchronize_session=False)
        # Finalmente, eliminar el evento
        dbsession.query(Evento).filter(Evento.id==evento).delete(synchronize_session=False)
        dbsession.commit()   

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@admin.route('/admin/AGuardarAsistencia')
def AGuardarAsistencia():
    #GET parameter
    participantes = request.args['participantes']
    results = [{'label':'/VParticipantes', 'msg':[ur'Registro exitoso']}, {'label':'/VParticipantes', 'msg':[ur'Registro no exitoso']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@admin.route('/admin/AModificarEvento/<idEvento>', methods=['POST'])
def AModificarEvento(idEvento):
    #GET parameter
    formulario = request.get_json()
    results = [{'label':'/VEvento/'+idEvento, 'msg':[ur'Evento modificado']}, {'label':'/VModificarEvento/'+idEvento, 'msg':[ur'Evento no modificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    evento = dbsession.query(Evento).get(idEvento)

    nro_personas_inscritas = evento.total_cupos - evento.cupos_disponibles
    fecha_evento = parseDate(formulario['fecha'])
    hoy = today()

    if evento.cupos_disponibles < 0:
        # Faltan pruebas
        res = results[1]
        res['msg'].append('Actualmente hay %s persona(s) inscritas. El nuevo número de cupos no pueder ser inferior a %s.' % \
            (nro_personas_inscritas, nro_personas_inscritas))
    elif fecha_evento < hoy:
        res = results[1]
        res['msg'].append('Fecha invalida')
    else:
        evento.nombre = formulario['nombreEvento']
        evento.descripcion = formulario['descripcion']
        evento.fecha = formulario['fecha']
        evento.lugar = formulario['lugar']
        evento.total_cupos = formulario['maxparticipantes']
        evento.cupos_disponibles = evento.total_cupos - nro_personas_inscritas
        dbsession.add(evento)
        dbsession.commit()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@admin.route('/admin/ARegistrarEvento', methods=['POST'])
def ARegistrarEvento():
    #GET parameter
    formulario = request.get_json()
    results = [{'label':'/VEvento', 'msg':[ur'Evento registrado']},
               {'label':'/VRegistroEvento', 'msg':[ur'Evento no registrado']},
               {'label':'/VRegistroEvento', 'msg':[ur'Fecha de evento no válida']},
              ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    n = formulario['nombreEvento']
    d = formulario['descripcion']
    f = formulario['fecha']
    l = formulario['lugar']
    c = formulario['maxparticipantes']
    
    # Verificar la fecha
    fecha_evento = parseDate(f)
    hoy = today()
    if fecha_evento < hoy:
        res = results[2]

    else:
        evento = Evento(afiche= '', nombre=n, descripcion=d, fecha=f, lugar=l, total_cupos=c, cupos_disponibles=c, administrador=session['correo'])
        dbsession.add(evento)
        dbsession.commit()
        res['label'] += '/' + str(evento.id)
	
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@admin.route('/admin/VAfiche')
def VAfiche():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VEvento/<idEvento>')
def VEvento(idEvento):
    res = {}

    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    e = dbsession.query(Evento).get(idEvento)
    a = dbsession.query(Actor).get(e.administrador)

    fecha_evento = parseDate(e.fecha)
    hoy = today()
    
    res['id'] = e.id
    res['nombreEvento'] = e.nombre
    res['descripcion'] = e.descripcion
    res['fecha'] = e.fecha
    res['lugar'] = e.lugar
    res['nroCupos'] = e.total_cupos
    res['cuposDisponibles'] = e.cupos_disponibles
    res['nombreAdmin'] = a.nombre
    res['abierto'] = fecha_evento >= hoy

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VInicioAdministrador')
def VInicioAdministrador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    eventos = dbsession.query(Evento).filter(Evento.administrador==session['correo'])
    
    res['eventos_abiertos'] = []
    res['eventos_cerrados'] = []

    hoy = today()
    for evento in eventos :
        fecha = parseDate(evento.fecha)

        if fecha < hoy:
            res['eventos_cerrados'].append({'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles})
        else:
            res['eventos_abiertos'].append({'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles})

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VModificarEvento/<idEvento>')
def VModificarEvento(idEvento):
    print "Entrando en rutina VModificarEvento con argumento %s" % idEvento
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    evento = dbsession.query(Evento).get(idEvento)

    res = { 'id': evento.id,
            'nombre': evento.nombre,
            'descripcion': evento.descripcion,
            'lugar': evento.lugar,
            'fecha': evento.fecha,
            'total_cupos':evento.total_cupos,
            'cupos_disponibles':evento.cupos_disponibles
    }

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VParticipantes/<idEvento>')
def VParticipantes(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    reservas = dbsession.query(Reserva).filter(Reserva.evento_id==idEvento)
    evento   = dbsession.query(Evento).get(idEvento)

    participantes = []

    for reserva in reservas:
        participante = dbsession.query(Actor).get(reserva.actor_correo)
        participantes.append({ 'correo' : participante.correo, 'nombre' : participante.nombre })

    res['participantes'] = participantes
    res['id'] = idEvento

    hoy = today()
    fecha_evento = parseDate(evento.fecha)

    res['cerrado'] = fecha_evento < hoy

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VRegistroEvento')
def VRegistroEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    hoy = today()

    res['hoy'] = dateToString(hoy)

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
