# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

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



@admin.route('/admin/AModificarEvento', methods=['POST'])
def AModificarEvento():
    #GET parameter
    formulario = request.args['formulario']
    results = [{'label':'/VEvento', 'msg':[ur'Evento modificado']}, {'label':'/VModificarEvento', 'msg':[ur'Evento no modificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


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
    formulario = request.args['formulario']
    results = [{'label':'/VEvento', 'msg':[ur'Evento registrado']}, {'label':'/VRegistroEvento', 'msg':[ur'Evento no registrado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


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



@admin.route('/admin/VEvento')
def VEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VInicioAdministrador')
def VInicioAdministrador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@admin.route('/admin/VModificarEvento')
def VModificarEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


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