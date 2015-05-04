from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta

app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

from app.phoenix.admin import admin
app.register_blueprint(admin)
from app.phoenix.usuario import usuario
app.register_blueprint(usuario)
from app.phoenix.login import login
app.register_blueprint(login)



#Application code starts here
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine =  create_engine('sqlite:///phoenix.db')

Base.prepare(engine, reflect=True)

Actor = Base.classes.actor
Evento = Base.classes.evento
Certificado = Base.classes.certificado
Reserva = Base.classes.reserva

session = Session(engine)

#Application code ends here

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()

