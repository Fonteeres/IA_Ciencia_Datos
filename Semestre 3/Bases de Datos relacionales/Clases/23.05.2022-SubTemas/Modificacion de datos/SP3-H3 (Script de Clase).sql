USE Ventas2

/*

Modificación de datos

*/

--
-- INSERT
--

SELECT * FROM MARCAS

INSERT INTO marcas 
	(marca, nombre, activo) 
VALUES 
	('V','NUEVA MARCA','N')

INSERT marcas
	(marca, nombre)
VALUES
	('W','WRANGLER')

TRUNCATE TABLE encargados

-- INSERT SELECT (Inserta en una tabla existente a partir de un select)

INSERT INTO encargados
SELECT 
	dni,
	nombre,
	ingreso,
	activo 
FROM 
	vendedores 
WHERE
	encargado = 'S'

-- SELECT INTO (Inserta y crea una tabla nueva a partir de un select)

SELECT
	dni,
	nombre,
	ingreso,
	activo
INTO 
	encargados
FROM
	vendedores 
WHERE 
	encargado = 'S'

SELECT * FROM ENCARGADOS

INSERT INTO encargados
	(dni,nombre,ingreso,activo)
VALUES
	(99999999,'ENCARGADO NUEVO',GETDATE(),'S')

SELECT 
	articulo,
	nombre
INTO
	temp_articulos
FROM 
	articulos
WHERE
	rubro = 78

INSERT 
	temp_articulos 
SELECT
	articulo,
	nombre
FROM 
	articulos
WHERE
	rubro = 25

select * from temp_articulos

drop table temp_articulos

drop table encargados

--
-- UPDATE
--

SELECT * FROM TEMP_MARCAS

drop table TEMP_MARCAS

SELECT * INTO temp_marcas FROM marcas

UPDATE temp_marcas
SET nombre = 'VANS', activo = 'S' 
WHERE
marca = 'V'

UPDATE temp_marcas
SET activo = 'S' 
WHERE
marca = 'W'

-- ROLLBACK / COMMIT

SELECT * FROM TEMP_SUCURSALES

SELECT * FROM SUCURSALES

DROP TABLE temp_sucursales

select *
into temp_sucursales 
from sucursales

UPDATE temp_sucursales
SET direccion = UPPER(direccion)

UPDATE temp_sucursales
SET direccion = LOWER(direccion)
WHERE sucursal = 8

UPDATE temp_sucursales
SET direccion = 'LOS ROBLES 228 - SAN LUIS'
WHERE sucursal = 7

--
-- DELETE / TRUNCATE
--

DELETE FROM marcas
WHERE marca IN('W','V')

SELECT * FROM MARCAS

TRUNCATE TABLE temp_sucursales


-- Ejemplo de borrado con INNER JOIN

DELETE vendet
--
FROM vendet as vd
INNER JOIN vencab as vc
ON vd.letra = vc.letra and vd.factura = vc.factura
WHERE
vc.fecha between ... and ...


/*

EJERCICIO 1: INSERTAR FILAS

a) Cree la tabla ACCESORIOS (rubros 76, 85, 77, 97, 70, 72, 87, 88) que tenga las columnas ARTICULO, NOMBRE,
PRECIOMAYOR y PRECIOMENOR tomando los datos de la tabla artículos. Utilice SELECT INTO.
b) Agregue a la tabla ACCESORIOS los artículos del rubro 89. Utilice INSERT SELECT.
c) Inserte un nuevo artículo con el código 'E000000001', denominado 'ELEMENTO ACCESORIO' con los precios 15 y 23.50
para ventas mayoristas y minoristas respectivamente.

En todos los casos verifique la correcta inserción de las filas mediante instrucciones SELECT de comprobación.

*/

-- a)



/*

EJERCICIO 2: MODIFICACIÓN DE DATOS

a) Usando la tabla ACCESORIOS creada anteriormente, modifique los artículos que tengan PRECIOMAYOR negativo
(menor a cero), reemplazando el valor negativo por cero (0)
b) Usando la tabla ACCESORIOS, reemplace el valor del PRECIOMENOR por PRECIOMAYOR * 1.10 (10% más) para
aquellos artículos en los que el PRECIOMENOR sea menor o igual al PRECIOMAYOR.

*/

-- a)

/*

EJERCICIO 3: ELIMINACION DE FILAS

a) Usando la tabla ACCESORIOS, borre las filas que correspondan a artículos que contengan la palabra OUTLET en su nombre
o que tengan valor cero en ambos precios (preciomayor y preciomenor)
b) Elimine la tabla ACCESORIOS.

*/

-- a)

-- b)

