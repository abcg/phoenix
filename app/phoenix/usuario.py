# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

usuario = Blueprint('usuario', __name__)


@usuario.route('/usuario/ADesconectarseUsuario')
def ADesconectarseUsuario():
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



@usuario.route('/usuario/AGenerarCertificado')
def AGenerarCertificado():
    #GET parameter
    evento = request.args['evento']
    results = [{'label':'/VEventoUsuario', 'msg':[ur'Generar certificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


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



@usuario.route('/usuario/VEventoUsuario')
def VEventoUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@usuario.route('/usuario/VInicioUsuario')
def VInicioUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here