# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from datetime import *
from models import *
admin = Blueprint('admin', __name__)


@admin.route('/admin/ADesconectarse')
def ADesconectarse():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPortada', 'msg':[ur'Usuario desconectado'], "actor":None}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


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

    evento.nombre = formulario['nombreEvento']
    evento.descripcion = formulario['descripcion']
    evento.fecha = formulario['fecha'] # CUIDADO QUE FALTA
    evento.lugar = formulario['lugar']
    evento.total_cupos = formulario['maxparticipantes']
    evento.cupos_disponibles = evento.total_cupos - nro_personas_inscritas

    if evento.cupos_disponibles < 0:
        # Faltan pruebas
        res = results[1]
        res['msg'].append('Actualmente hay %s persona(s) inscritas. El nuevo número de cupos no pueder ser inferior a %s.' % \
            (nro_personas_inscritas, nro_personas_inscritas))
    else:
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
    results = [{'label':'/VEvento', 'msg':[ur'Evento registrado']}, {'label':'/VRegistroEvento', 'msg':[ur'Evento no registrado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    n = formulario['nombreEvento']
    d = formulario['descripcion']
    f = formulario['fecha']
    l = formulario['lugar']
    c = formulario['maxparticipantes']
	
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
    
    res['id'] = e.id
    res['nombreEvento'] = e.nombre
    res['descripcion'] = e.descripcion
    res['lugar'] = e.lugar
    res['nroCupos'] = e.total_cupos
    res['cuposDisponibles'] = e.cupos_disponibles
    res['nombreAdmin'] = a.nombre

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VInicioAdministrador')
def VInicioAdministrador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    aux = dbsession.query(Evento).filter(Evento.administrador==session['correo'])
    
    res['eventos'] = []
    for evento in aux :
        res['eventos'].append({'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles})

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



@admin.route('/admin/VParticipantes')
def VParticipantes():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VRegistroEvento')
def VRegistroEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
