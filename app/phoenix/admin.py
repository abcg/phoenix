# -*- coding: utf-8 -*-
import os
from flask import request, session, Blueprint, json, current_app, send_from_directory
from werkzeug import secure_filename
from models import *
from dateManager import *


admin = Blueprint('admin', __name__)


@admin.route('/admin/ADesconectarse')
def ADesconectarse():
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



@admin.route('/admin/AEliminarEvento')
def AEliminarEvento():
    #GET parameter
    evento = request.args['evento']
    results = [{'label':'/VInicioAdministrador', 'msg':[ur'Evento eliminado.']},
               {'label':'/VEvento', 'msg':[ur'Evento no eliminado.']},
               {'label':'/VEvento', 'msg':[ur'Eliminación sin efecto. No se puede eliminar un evento realizado.']},
              ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    e = dbsession.query(Evento).get(evento)
    hoy = today()
    fecha_evento = parseDate(e.fecha)

    if fecha_evento < hoy:
        res = results[2]

    else:
        # Primero, eliminar las reservas asociadas al evento
        dbsession.query(Reserva).filter(Reserva.evento_id==evento).delete(synchronize_session=False)

        if e.afiche:
            os.remove(e.afiche)

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



@admin.route('/admin/AGuardarAsistencia', methods=['POST'])
def AGuardarAsistencia():
    #GET parameter
    asistencia_info = request.get_json()
    results = [{'label':'/VParticipantes', 'msg':[ur'Registro de asistencia exitoso.']},
               {'label':'/VParticipantes', 'msg':[ur'Hubo un error al registrar la asistencia.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    evento = dbsession.query(Evento).get(asistencia_info['evento'])

    for correo in asistencia_info['asistencia'].keys():
        reserva = dbsession.query(Reserva).get((correo, evento.id))
        reserva.asistencia = 1
        dbsession.add(reserva)

    evento.cerrado = 1
    dbsession.add(evento)
    dbsession.commit()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@admin.route('/admin/AModificarEvento', methods=['POST'])
def AModificarEvento():
    #GET parameter
    #formulario = request.get_json()
    evento_id = request.form['id']
    results = [{'label':'/VEvento/'+evento_id, 'msg':[ur'¡Modificación exitosa!']},
               {'label':'/VModificarEvento/'+evento_id, 'msg':[ur'La modificación no tuvo éxito.']},
               {'label':'/VModificarEvento/'+evento_id, 'msg':[ur'El afiche debe ser un archivo PDF.']},
    ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    evento = dbsession.query(Evento).get(evento_id)

    nro_personas_inscritas = evento.total_cupos - evento.cupos_disponibles

    fecha_evento = parseDate(request.form['fecha'])
    hoy = today()

    if nro_personas_inscritas > request.form['maxparticipantes']:
        res = results[1]
        res['msg'].append('Actualmente hay %s persona(s) inscrita(s). El nuevo número de cupos no pueder ser inferior a %s.' % \
            (nro_personas_inscritas, nro_personas_inscritas))

    elif fecha_evento < hoy:
        res = results[1]
        res['msg'].append('Fecha invalida')

    else:
        evento.nombre = request.form['nombreEvento']
        evento.fecha = request.form['fecha']
        evento.lugar = request.form['lugar']
        evento.total_cupos = int(request.form['maxparticipantes'])
        evento.descripcion = request.form['descripcion']
        evento.cupos_disponibles = evento.total_cupos - nro_personas_inscritas
        file = request.files.get('archivo', None)

        if file:
            if allowed_file(file.filename):
                filename = afiche_filename(evento.id, secure_filename(file.filename))
                path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

                if evento.afiche :
                  os.remove(evento.afiche)
              
                file.save(path)
                evento.afiche = path
                dbsession.add(evento)
                dbsession.commit()
            else:
                res = results[2]
            
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
    #formulario = request.get_json()
    results = [{'label':'/VEvento', 'msg':[ur'Evento "%s" registrado.' % (request.form['nombreEvento'])]},
               {'label':'/VRegistroEvento', 'msg':[ur'Evento no registrado.']},
               {'label':'/VRegistroEvento', 'msg':[ur'Fecha de evento no válida.']},
               {'label':'/VRegistroEvento', 'msg':[ur'El afiche debe ser un archivo PDF.']},
              ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    n = request.form['nombreEvento']
    d = request.form['descripcion']
    f = request.form['fecha']
    l = request.form['lugar']
    c = int(request.form['maxparticipantes'])
    file = request.files.get('archivo', None)
    
    # Verificar la fecha
    fecha_evento = parseDate(f)
    hoy = today()
    if fecha_evento < hoy:
        res = results[2]

    else:
        evento = Evento(afiche='', nombre=n, descripcion=d, fecha=f, lugar=l, total_cupos=c, cupos_disponibles=c, administrador=session['correo'], cerrado=0)

        if file:
            if allowed_file(file.filename):
                dbsession.add(evento)
                dbsession.flush()
                filename = afiche_filename(evento.id, secure_filename(file.filename))

                path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(path)

                evento.afiche = path

                dbsession.add(evento)
                dbsession.commit()
                res['label'] += '/' + str(evento.id)
            else:
                res = results[3]
        else:
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



@admin.route('/admin/VAfiche/<idEvento>')
def VAfiche(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    evento = dbsession.query(Evento).get(idEvento)

    res['afiche'] = evento.afiche
    res['id'] = evento.id

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
    res['afiche'] = e.afiche

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
        info = {'id':evento.id, 'nombre':evento.nombre, 'fecha':evento.fecha, 'cupos_disponibles':evento.cupos_disponibles}
        if fecha < hoy:
            res['eventos_cerrados'].append(info)
        else:
            res['eventos_abiertos'].append(info)

    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VModificarEvento/<idEvento>')
def VModificarEvento(idEvento):
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    evento = dbsession.query(Evento).get(idEvento)

    res['id'] =  evento.id
    res['nombre'] = evento.nombre
    res['descripcion'] = evento.descripcion
    res['lugar'] = evento.lugar
    res['fecha'] = evento.fecha
    res['total_cupos'] = evento.total_cupos
    res['cupos_disponibles'] = evento.cupos_disponibles

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
    res['realizado'] = fecha_evento < hoy
    res['cerrado'] = evento.cerrado

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

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

def afiche_filename(i, s):
    return str(i) + "_" + s

@admin.route('/uploads/<afiche>')
def getAfiche(afiche):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], str(afiche))

#Use case code ends here
