from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine('sqlite:///phoenix.db')

Base.prepare(engine, reflect=True)

Actor = Base.classes.actor
Evento = Base.classes.evento
Certificado = Base.classes.certificado
Reserva = Base.classes.reserva

dbsession = Session(engine)
