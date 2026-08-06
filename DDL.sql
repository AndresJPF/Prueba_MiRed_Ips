-- Base de Datos

CREATE DATABASE IF NOT EXISTS mired_ips
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE mired_ips;

-- Tabla: users

CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    role ENUM('admin', 'empleado')
        NOT NULL
        DEFAULT 'empleado',

    remember_token VARCHAR(100) NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    deleted_at TIMESTAMP NULL
);


-- Tabla: categorias

CREATE TABLE categorias (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL UNIQUE,

    descripcion TEXT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);


-- Tabla: productos

CREATE TABLE productos (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    codigo VARCHAR(20) NOT NULL UNIQUE,

    nombre VARCHAR(150) NOT NULL,

    categoria_id BIGINT UNSIGNED NOT NULL,

    descripcion TEXT NULL,

    precio DECIMAL(10,2) NOT NULL,

    stock INT UNSIGNED NOT NULL DEFAULT 0,

    estado ENUM('activo', 'inactivo')
        NOT NULL
        DEFAULT 'activo',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_producto_categoria
        FOREIGN KEY (categoria_id)
        REFERENCES categorias(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Índices

CREATE INDEX idx_users_role
ON users(role);

CREATE INDEX idx_productos_categoria
ON productos(categoria_id);

CREATE INDEX idx_productos_estado
ON productos(estado);

CREATE INDEX idx_productos_nombre
ON productos(nombre);