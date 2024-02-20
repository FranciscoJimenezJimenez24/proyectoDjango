create table if not exists deportes (
	id_deporte int primary key auto_increment,
    nombre varchar(20) not null unique
);

create table if not exists instalaciones (
	id_instalacion int primary key auto_increment,
    nombre varchar(20) not null unique,
    direccion varchar(100) not null,
    iluminacion boolean not null default false,
    cubierta boolean not null default false
);

create table if not exists equipos (
	id_equipo int primary key auto_increment,
    nombre varchar(20) not null unique,
    id_deporte int not null,
    equipacion_principal varchar(100) not null,
    equipacion_suplente varchar(100) not null,
    contacto varchar(100) not null,
    telefono varchar(15) not null,
    email varchar(100) not null,
    foreign key (id_deporte) references deportes(id_deporte) on delete restrict on update cascade
);

create table if not exists jugadores (
	id_jugador int primary key auto_increment,
    nombre varchar(20) not null,
    apellido1 varchar(20) not null,
    apellido2 varchar(20),
    id_equipo int not null,
    dorsal int not null,
    fecha_nacimiento date not null,
    altura decimal(3,2) not null check (altura > 0),
    peso int not null check (peso > 0),
    telefono varchar(15) not null,
    foreign key (id_equipo) references equipos(id_equipo) on delete restrict on update cascade
);

-- Índice para evitar que un dorsal se repita en un equipo
create unique index idx_equipo_dorsal on jugadores(id_equipo, dorsal);

create table if not exists partidos (
	id_partido int primary key auto_increment,
    id_deporte int not null,
    fecha_hora datetime not null,
    id_instalacion int,
    id_local int not null,
    id_visitante int not null,
    puntos_local int check (puntos_local >= 0),
    puntos_visitante int check (puntos_visitante >= 0),
    observaciones varchar(200),
    foreign key (id_deporte) references deportes(id_deporte) on delete restrict on update cascade,
    foreign key (id_instalacion) references instalaciones(id_instalacion) on delete restrict on update cascade,
    foreign key (id_local) references equipos(id_equipo) on delete restrict on update cascade,
    foreign key (id_visitante) references equipos(id_equipo) on delete restrict on update cascade
);
