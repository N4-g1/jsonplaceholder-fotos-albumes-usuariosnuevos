create database jsonplaceholder_db;


CREATE TABLE albums (
    id INT PRIMARY KEY,
    userId INT NOT NULL,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE photos (
    id INT PRIMARY KEY,
    albumId INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(500) NOT NULL,
    thumbnailUrl VARCHAR(500) NOT NULL,
    -- Definición de la relación
    CONSTRAINT fk_album
        FOREIGN KEY (albumId) 
        REFERENCES albums(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    contrasena_salt VARCHAR(255) NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
);

ALTER TABLE usuarios DROP COLUMN contrasena_salt;


