# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

login = Blueprint('login', __name__)


@login.route('/login/AIdentificar', methods=['POST'])
def AIdentificar():
    #GET parameter
    login, clave = request.args['login, clave']
    results = [{'label':'/VInicioAdministrador', 'msg':[ur'Administrador identificado'], "actor":"actor_administrador"}, {'label':'/VInicioUsuario', 'msg':[ur'Usuario identificado'], "actor":"actor_usuario"}, {'label':'/VPortada', 'msg':[ur'Error en identificacion']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@login.route('/login/ARegistrarUsuario', methods=['POST'])
def ARegistrarUsuario():
    #GET parameter
    login, correo, clave = request.args['login, correo, clave']
    results = [{'label':'/VPortada', 'msg':[ur'Usuario registrado'], "actor":"actor_usuario"}, {'label':'/VRegistroUsuario', 'msg':[ur'Usuario no registrado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@login.route('/login/VPortada')
def VPortada():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@login.route('/login/VRegistroUsuario')
def VRegistroUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here