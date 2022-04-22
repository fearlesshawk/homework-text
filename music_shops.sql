create table if not exists albums (
	id serial NOT NULL,
	namealbums varchar(40) NOT NULL,
	releaseyearalbums int NOT NULL,
	CONSTRAINT albums_pk PRIMARY KEY (id)
);

create table if not exists artist (
	id serial NOT NULL,
	nameartists varchar(40) NOT NULL,
	CONSTRAINT artist_pk PRIMARY KEY (id)
);

create table if not exists genres (
	id serial NOT NULL,
	namegenres varchar(40) NOT NULL,
	CONSTRAINT genres_pk PRIMARY KEY (id)
);

create table if not exists tracks (
	id serial NOT NULL,
	nametracks varchar(40) NOT NULL,
	duration time NOT NULL,
	idalbums int NOT NULL,
	CONSTRAINT tracks_pk PRIMARY KEY (id),
	CONSTRAINT tracks_id_fkey FOREIGN KEY (idalbums) REFERENCES albums(id)
);

create table if not exists Mixtapes (
	id serial NOT NULL,
	namemixtapes varchar(40) NOT NULL,
	releaseyearmixtapes int4 NOT NULL,
	CONSTRAINT Mixtapes_pk PRIMARY KEY (id)
	);

create table if not exists ArtistsAlbums (
	artists_id integer references artist(id),
	albums_id integer references albums(id),
	constraint ArtistsAlbums_pk primary key (artists_id, albums_id)
	);
	
create table if not exists ArtistsGenres (
	artists_id integer references artist(id),
	genres_id integer references genres(id),
	constraint ArtistsGenres_pk primary key (artists_id, genres_id)
	);
	
create table if not exists MixtapesTracks (
	mixtapes_id integer references mixtapes(id),
	tracks_id integer references tracks(id),
	constraint MixtapesTracks_pk primary key (mixtapes_id, tracks_id)
	);
