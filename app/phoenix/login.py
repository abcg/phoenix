# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from models import *

login = Blueprint('login', __name__)


@login.route('/login/AIdentificar', methods=['POST'])
def AIdentificar():
    #GET parameter
    formulario = request.get_json()
    results = [{'label':'/VInicioAdministrador', 'msg':[], "actor":"actor_administrador"},
               {'label':'/VInicioUsuario', 'msg':[], "actor":"actor_usuario"},
               {'label':'/VPortada', 'msg':[ur'Error: combinación incorrecta de correo y clave.']},
    ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    correo = formulario['correo'].lower()
    clave  = formulario['clave']
    actor  = dbsession.query(Actor).get(correo)

    if actor is not None and actor.clave == clave:
        if not actor.es_administrador:
            res = results[1]
        res['msg'].append('¡Hola, %s!' % (str(actor.nombre)))
        session['usuario'] = actor.nombre
        session['correo']  = actor.correo
    else:
        res = results[2]

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
    formulario = request.get_json()
    results = [{'label':'/VPortada', 'msg':[ur'Usuario %s (%s) registrado.' % (formulario['nombre'], formulario['correo'])], "actor":"actor_usuario"},
               {'label':'/VRegistroUsuario', 'msg':[ur'Usuario no registrado']},
    ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    if dbsession.query(Actor).get(formulario['correo']) is not None:
        res = results[1]
        res['msg'].append('Ya existe un usuario registrado con el correo \'%s\'' % (formulario['correo']))
    else:
        dbsession.add(Actor(correo=formulario['correo'].lower(), clave=formulario['clave'], nombre=formulario['nombre'], es_administrador=formulario['esAdministrador']))
        dbsession.commit()

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
