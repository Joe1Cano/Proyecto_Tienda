create database tienda;

use tienda;

CREATE TABLE clientes (
    noClientes int not null AUTO_INCREMENT,
    nombre varchar(20) not null,
    apellido VARCHAR(30) not null,
    correo VARCHAR(40) not null,
    telefono VARCHAR(20) not null,
    primary key(noClientes)  
);

CREATE TABLE movimientos(
    noMovimientos int not null AUTO_INCREMENT,
    noProductos int not null,
    tipo varchar(10) not null,
    fecha date not null,
    cantidad int not null,
    primary key(noMovimientos)  
);

CREATE TABLE productos(
    noProductos int not null AUTO_INCREMENT,
    nombre varchar(20) not null,
    precio int not null,
    cantidad int not null,
    noProveedor int not null,
    costo int not null,
    primary key(noProductos)  
);


CREATE TABLE proveedores(
    noProveedores int not null AUTO_INCREMENT,
    nombre varchar(20) not null,
    apellido VARCHAR(30) not null,
    correo VARCHAR(40) not null,
    telefono VARCHAR(20) not null,
    primary key(noProveedores)  
);

CREATE TABLE ventas(
    noVentas int not null AUTO_INCREMENT,
    noProductos int not null,
    fecha date not null,
    cantidad int not null,
    precio int not null,
    subtotal double not null,
    primary key(noVentas)  
);


DELIMITER $$
DROP PROCEDURE IF EXISTS `altaClientes`$$
CREATE PROCEDURE altaClientes()
BEGIN
    INSERT INTO clientes (nombre, apellido, correo, telefono) VALUES (_name, _apellido,_correo,_telefono);
END;
$$

DELIMITER $$
DROP TRIGGER IF EXISTS `crearSalida`$$
CREATE TRIGGER crearSalida AFTER INSERT ON `ventas` FOR EACH ROW 
	INSERT into movimientos (noProductos, tipo, fecha, cantidad) VALUES (new.noProductos, "salida", new.fecha, new.cantidad);
END;
$$

DELIMITER $$
DROP TRIGGER IF EXISTS `crearSubtotal`$$
CREATE TRIGGER crearSubtotal BEFORE INSERT ON `ventas` FOR EACH ROW 
IF
    new.cantidad > 0 THEN
    set new.subtotal = new.cantidad * new.precio;
    ELSEIF
    new.precio > 0 THEN
    set new.subtotal = new.cantidad * new.precio;
END if;
$$