DROP TABLE IF EXISTS actor;
CREATE TABLE actor (
  login  text not null primary key,
  clave  text not null,
  correo text not null,
  es_administrador integer not null
);

DROP TABLE IF EXISTS evento;
CREATE TABLE evento (
  id                integer primary key autoincrement,
  nombre            text not null,
  descripcion       text not null,
  afiche            text not null,
  lugar             text not null,
  fecha             text not null,
  total_cupos       integer not null,
  cupos_disponibles integer not null,
  administrador     integer not null,
  FOREIGN KEY(administrador) REFERENCES actor(login)
);

DROP TABLE IF EXISTS certificado;
CREATE TABLE certificado (
  id                  integer primary key autoincrement,
  fecha_de_generacion text not null,

  -- reserva asociada
  actor_login text not null,
  evento_id  text not null,
  FOREIGN KEY(actor_login, evento_id) REFERENCES reserva(actor_login, evento_id)
);

DROP TABLE IF EXISTS reserva;
CREATE TABLE reserva (
  actor_login text not null,
  evento_id  text not null,
  asistencia integer,
  PRIMARY KEY (actor_login, evento_id),
  FOREIGN KEY(actor_login) REFERENCES actor(login),
  FOREIGN KEY(evento_id)     REFERENCES evento(id)
);

