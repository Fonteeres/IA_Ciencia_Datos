/*

- Transacciones
- Procedimientos almacenados

*/

use Ventas2
select * from marcas
select * from rubros
select * from articulos

--
-- TRANSACCIONES (TRANSACT SQL) - EJEMPLO 1
--

BEGIN TRANSACTION

UPDATE marcas
SET nombre = 'WRANGLER'
WHERE marca = 'W'

--DELETE FROM marcas
--WHERE nombre = 'YON FUS'

INSERT marcas
(marca,nombre,activo)
VALUES
('W','WRANGLER','S')

--INSERT marcas
--VALUES
--('Y','YON FUS','N') 

IF @@ERROR <> 0 --@@ERROR es una funci�n de configuraci�n de SQL Server que devuelve el c�digo del error retornado
	BEGIN 
		RAISERROR ('Error, transacci�n no completada! :-(', 16, -1) 
		--PRINT 'La transacci�n FALLO!!!'
		ROLLBACK TRANSACTION 
	END 
ELSE
	BEGIN
		PRINT 'La transacci�n se complet� con �xito!!!'
		COMMIT TRANSACTION
	END

--
-- TRANSACCIONES (TRANSACT SQL) - EJEMPLO 2
--

DECLARE 
	@E int,
	@D nchar(30)

BEGIN TRANSACTION
 
INSERT marcas
VALUES
('Y','YON FUS','N') 

--PRINT 'El error que di� fue: ' + STR(@@ERROR)

SET @E = @@ERROR
SET @D = 'N�MERO DE ERROR: '
 
IF @E <> 0 --@@ERROR YA SE BLANQUE�
	BEGIN 
		--PRINT STR(@E)
		PRINT RTRIM(@D) + ' (' + LTRIM(STR(@E)) + ')'
		ROLLBACK TRANSACTION
	END
ELSE
	BEGIN
		PRINT 'La transacci�n se realiz�n con �xito :-)'
		COMMIT TRANSACTION
	END

--
-- STORED PROCEDURES (Procedimientos Almacenados)
--

DROP PROCEDURE sp_cuentavendedores


CREATE OR ALTER PROCEDURE sp_cuentavendedores AS
BEGIN
	SELECT COUNT(*) AS "Filas" FROM vendedores
END

CREATE OR ALTER PROCEDURE sp_cuentavendedores
-- @fd smalldatetime,
-- @fh smalldatetime,
-- @c int OUTPUT
AS
--DECLARE
--	@c int
BEGIN
	SELECT * FROM vendedores
--	SELECT @c = COUNT(*)
--  FROM vendedores
	--
	--PRINT STR(@c)
	--PRINT 'La tabla vendedores tiene ' + TRIM(STR(@c)) + ' filas.'
	--RETURN (@@ROWCOUNT)
	PRINT 'Rowcount es igual a ' + TRIM(STR(@@ROWCOUNT))
END

-- EJECUCI�N SIN PAR�METROS

EXEC sp_cuentavendedores

-- EJECUCI�N CON PAR�METRO DE SALIDA

DECLARE @pepe int
EXEC sp_cuentavendedores @pepe OUTPUT
PRINT 'La tabla vendedores tiene ' + TRIM(STR(@pepe)) + ' filas.'


/*

Construir el SP que permita insertar una nueva marca, solicitando como par�metros los tres valores, y que devuelva el mensaje
'La marca [nombre] se insert� correctamente', pero si no presentar el mensaje 'Hubo un problema! No se pudo insertar la marca.'

*/

CREATE OR ALTER PROCEDURE sp_insertar_marca
	@marca char(1), 
	@nombre char(30),
	@activo char(1)
AS
BEGIN

	IF EXISTS (SELECT * FROM marcas WHERE marca = @marca)
		PRINT 'La marca ' + TRIM(@marca) + ' ya existe.'
	ELSE 
		BEGIN
			INSERT INTO marcas
			(marca, nombre, activo)
			VALUES
			(@marca,@nombre,@activo)
			--
			IF @@ERROR <> 0
				PRINT 'Hubo un problema! No se pudo insertar la marca.'
			ELSE
				PRINT 'La marca ' + TRIM(@nombre) + ' se insert� correctamente.'
		END
END

EXEC sp_insertar_marca 'W','WRANGLER','S'

SELECT * FROM marcas

DELETE marcas WHERE marca IN ('X','W','Y')

SELECT @@VERSION

SELECT @@ERROR

SELECT @@LANGUAGE

SELECT @@TRANCOUNT

COMMIT TRANSACTION

SELECT * FROM PIRULO

EXEC sp_databases

EXEC sp_columns marcas