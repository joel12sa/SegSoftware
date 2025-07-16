CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    cedula VARCHAR(13) NOT NULL UNIQUE,
    telefono VARCHAR(10) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero VARCHAR(10) NOT NULL,
    direccion VARCHAR(50) NOT NULL,
    salario FLOAT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    sitio_web VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL
);