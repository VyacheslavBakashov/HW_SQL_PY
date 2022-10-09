CREATE TABLE IF NOT EXISTS genre (
	genre_id SERIAL PRIMARY KEY,
	name_genre VARCHAR(40) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS singer (
	singer_id SERIAL PRIMARY KEY,
	name_singer VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	album_id SERIAL PRIMARY KEY,
	name_album VARCHAR(60),
	date_release DATE,
				 CONSTRAINT album_minimum_year
				 CHECK (EXTRACT(YEAR FROM date_release) > 1950)
);

CREATE TABLE IF NOT EXISTS track (
	track_id SERIAL PRIMARY KEY,
	name_track VARCHAR(100),
	duration FLOAT,
	    	 CONSTRAINT minimum_duration
	 		 CHECK (duration > 60),
	album_id INTEGER NOT NULL REFERENCES album(album_id)
);

CREATE TABLE IF NOT EXISTS collection (
	collection_id SERIAL PRIMARY KEY,
	name_collection VARCHAR(80),
	date_release DATE,
				 CONSTRAINT collection_minimum_year
				 CHECK (EXTRACT(YEAR FROM date_release) > 1950)
);

CREATE TABLE IF NOT EXISTS collection_track (
	collection_id INTEGER NOT NULL REFERENCES collection(collection_id),
	track_id INTEGER NOT NULL REFERENCES track(track_id),
	CONSTRAINT ct PRIMARY KEY (collection_id, track_id)
);

CREATE TABLE IF NOT EXISTS singer_album (
	singer_id INTEGER NOT NULL REFERENCES singer(singer_id),
	album_id INTEGER NOT NULL REFERENCES album(album_id),
	CONSTRAINT sa PRIMARY KEY (singer_id, album_id)
);

CREATE TABLE IF NOT EXISTS genre_singer (
	genre_id INTEGER NOT NULL REFERENCES genre(genre_id),
	singer_id INTEGER NOT NULL REFERENCES singer(singer_id),
	CONSTRAINT pk PRIMARY KEY (genre_id, singer_id)
);
