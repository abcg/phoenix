DROP TABLE IF EXISTS actor;
CREATE TABLE actor (
  correo text not null primary key,
  nombre text not null,
  clave  text not null,
  es_administrador integer not null
);

DROP TABLE IF EXISTS evento;
CREATE TABLE evento (
  id                integer primary key autoincrement,
  nombre            text not null,
  descripcion       text not null,
  afiche            text not null,
  lugar             text not null,
  fecha             integer not null,
  total_cupos       integer not null,
  cupos_disponibles integer not null,
  administrador     text not null,
  FOREIGN KEY(administrador) REFERENCES actor(correo)
);

DROP TABLE IF EXISTS certificado;
CREATE TABLE certificado (
  id                  integer primary key autoincrement,
  fecha_de_generacion text not null,

  -- reserva asociada
  actor_correo text not null,
  evento_id  text not null,
  FOREIGN KEY(actor_correo, evento_id) REFERENCES reserva(actor_correo, evento_id)
);

DROP TABLE IF EXISTS reserva;
CREATE TABLE reserva (
  actor_correo text not null,
  evento_id  text not null,
  asistencia integer,
  PRIMARY KEY (actor_correo, evento_id),
  FOREIGN KEY(actor_correo) REFERENCES actor(correo),
  FOREIGN KEY(evento_id)     REFERENCES evento(id)
);

