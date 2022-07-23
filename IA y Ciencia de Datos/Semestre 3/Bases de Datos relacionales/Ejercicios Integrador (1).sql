/*

1. RECUPERACIÓN DE DATOS SIMPLE

Listar todos los artículos que cumplan con las siguientes condiciones:
- su preciomenor tenga un valor entre 5.00 y 30.00
- su código (articulo) comience con la letra K
- contenga en su nombre la palabra REMERA

Presentar las columnas ARTICULO, NOMBRE, PRECIOMENOR y ESTADO. Ordenar por la columna NOMBRE.

TABLAS: articulos (EL RESULTADO DEBE ARROJAR 31 FILAS)

*/
SELECT
	articulo,
	nombre,
	preciomenor,
	estado
FROM articulos
WHERE
	preciomenor between 5.00 and 30.0 and
	articulo like '%K%' and
	nombre like '%REMERA%'
order by
	2
/*

2. RECUPERACIÓN DE DATOS CON AGRUPAMIENTO

Mostrar por MES la cantidad de facturas emitidas y el importe total de ventas MAYORISTAS correspondientes al año 2007.

Excluir las ventas anuladas. Mostrar las columnas MES, FACTURAS, IMPORTE. Ordenar por mes.

TABLAS: mayorcab (EL RESULTADO DEBE ARROJAR 12 FILAS)

*/
Select
	month(Fecha) AS Mes,
	count(factura) as TotalFacturas,
	sum(total) as Importe
FROM mayorcab
where
	YEAR(fecha) = 2007 and
	anulada = 0
group by
	month(Fecha)
order by
	1
/*

3. RECUPERACIÓN DE DATOS CON SUBCONSULTA

Listar los vendedores ACTIVOS que NO realizaron ventas minoristas en el periodo que va del 01/04/2006 al 30/06/2006.

Mostrar las columnas VENDEDOR (código), NOMBRE, ENCARGADO y ACTIVO. Ordenar por nombre del vendedor.

TABLAS: vencab (suconsulta), vendedores (consulta principal) (EL RESULTADO DEBE RETORNAR 68 FILAS)

*/
Select*from vencab where fecha between '04-01-2006' and '06-30-2006'
select*from vendedores
SELECT
	DISTINCT
	vendedor,
	nombre,
	encargado,
	activo
From vendedores 
where
	activo = 'S' and
	 vendedor not in (Select Distinct vendedor From vencab where fecha between '04-01-2006' and '06-30-2006')
order by
	2
/*

4. RECUPERACIÓN DE DATOS CON UNION

Listar en una sola columna denominada "Factura" la LETRA + FACTURA (concatenadas) de las facturas realizadas por ventas minoristas
(vencab) en el mes de mayo del 2006, excluyendo las ventas anuladas. 

Luego listar el conjunto equivalente pero para ventas mayoristas (mayorcab), para el mismo periodo y excluyendo también
ventas anuladas.

Unir los dos conjuntos, agregando una columna "Tipo Venta" que indique si la factura es de venta mayorista o minorista.

Ordenar por la primer columna "Factura".

TABLAS: vencab (consulta 1), mayorcab (consulta 2) (EL RESULTADO DEBE RETORNAR 10738 FILAS)

*/
Select
	ltrim(rtrim(letra)) + ltrim(rtrim(str(factura))) as Factura,
	'MIN' as 'Tipo Venta'
FROM
	vencab
Where
	MONTH(fecha) = 5 and
	Year(fecha) = 2006 and
	anulada = 0
Union

Select
	ltrim(rtrim(letra)) + ltrim(rtrim(str(factura))) as Factura,
	'MAY' as 'Tipo Venta'
FROM
	mayorcab
WHERE
	MONTH(fecha) = 5 and
	Year(fecha) = 2006
	and anulada = 0
order by
	2
/*

5. RECUPERACIÓN DE DATOS DE VARIAS TABLAS

Listar las facturas de ventas MAYORISTAS, generadas en el año 2007 por clientes de la provincia de Córdoba.

Los clientes de la provincia de Córdoba son aquellos cuyo código postal (columna CP de la tabla CLIENTES) 
está entre '5000' y '5999'. TENGA EN CUENTA QUE ESTA COLUMNA ES DE TIPO CHAR.

Mostrar en el resultado las columnas NOMBRE (cliente), CP, LETRA, FACTURA, FECHA y TOTAL.

Ordene por el nombre del cliente, y luego por el número de factura. Excluya ventas anuladas.

TABLAS: clientes, mayorcab (EL RESULTADO DEBE RETORNAR 5327 FILAS)

*/
Select
	c.nombre,
	c.cp,
	mc.letra,
	mc.factura,
	mc.fecha,
	mc.total
From clientes c
	inner join mayorcab mc on (c.cliente = mc.cliente)
where
	anulada = 0
	and c.cp between '5000' and '5999'
	and YEAR(fecha) = 2007
order by
	1,4
/*

6. RECUPERACIÓN DE DATOS DE VARIAS TABLAS CON AGRUPAMIENTO

Partiendo de la base de la consulta anterior (con las mismas condiciones), muestre ahora las siguientes columnas: 

NOMBRE (cliente), CP, CANTIDAD DE FACTURAS (count), IMPORTE TOTAL (sum)

Ordene en forma DESCENDENTE por el IMPORTE TOTAL.

TABLAS: clientes, mayorcab (EL RESULTADO DEBE RETORNAR 142 FILAS)

*/
Select
	c.nombre,
	c.cp,
	count(mc.factura) as 'Cantidad Facturas',
	Sum(mc.total) as 'Total'
From clientes c
	inner join mayorcab mc on (c.cliente = mc.cliente)
where
	anulada = 0
	and c.cp between '5000' and '5999'
	and YEAR(fecha) = 2007
group by
	c.nombre,
	c.cp
order by
	4 desc
/*

7. RECUPERACIÓN DE DATOS DE VARIAS TABLAS CON SUBCONSULTA Y AGRUPAMIENTO

El vendedor SIKORA ARIEL (144) fue quien mas ventas logró en el año 2005 (en importe total). 

Se le solicita determinar qué vendedores lo superaron (en importe total) en el año 2006. Debe excluir ventas anuladas en todas las consultas.

Mostrar VENDEDOR, NOMBRE, ENCARGADO (S o N), IMPORTE TOTAL. Ordene el resultado por importe total en forma decreciente.

TABLAS: vencab y vendedores (consulta principal), vencab (subconsulta). EL RESULTADO DEBE RETORNAR 4 FILAS.

*/
SELECT
	v.vendedor,
	v.nombre,
	v.encargado,
	sum(vc.total) as 'Importe Total'
FROM vencab vc
	inner join vendedores v on (vc.vendedor = v.vendedor) 
where
	year(fecha) = 2006
	 and vc.anulada = 0
group by
	v.vendedor,
	v.nombre,
	v.encargado
having 
	sum(vc.total) > (Select sum(total) from vencab where anulada = 0 and vendedor = 144 and year(fecha) = 2005) 
order by
	4 desc
/*

8. INSERCIÓN SIMPLE

En la empresa ha ingresado un nuevo vendedor: LASPINA MARCELA (dni 30401211). Realice la instrucción correspondiente para 
darla de alta en la tabla VENDEDORES, teniendo en cuenta:
	- Determine previamente en una consulta el código (columna VENDEDOR) que le correspondería, sumándole 1 al máximo valor.
	- La sucursal donde ingresa es VILLA CABRERA (determine el código previamente)
	- La fecha de ingreso debe ser tomada en el momento de la inserción.
	- El nuevo vendedor deberá estar ACTIVO (activo = 'S'), y será ENCARGADO (encargado = 'S').

*/
Select max(vendedor)+1 From vendedores
Select sucursal,denominacion from sucursales where denominacion like '%VILLA CABRERA%'
Select * From vendedores

insert into vendedores
	(vendedor,nombre,sucursal,dni,ingreso,encargado,activo)
VALUES
	(1051,'LASPINA MARCELA',5,30401211,GETDATE(),'S','S')

SELECT * From vendedores where vendedor = 1051
/*

9. INSERCIÓN MASIVA CON CREACIÓN DE TABLA

Utilizando SELECT..INTO cree la tabla TmpVentasAccesorios. Esta tabla debe mostrar el total de ventas por rubro de
artículo. Deberá incluir solamente los rubros: 76, 85, 77, 97, 70, 72, 87, 88.

La estructura de la tabla debe ser RUBRO (código), NOMBRE, TOTAL (el total vendido de ese rubro). Tenga en cuenta:
	- Excluya ventas anuladas.
	- La nueva tabla deberá tener UNA FILA POR RUBRO, mostrando el importe total vendido.
	- Calcular el total vendido utilizando CANTIDAD * PRECIO de la tabla VENDET.

TABLAS: rubros, vencab, vendet, articulos (para el SELECT CON AGRUPAMIENTO). 

LA NUEVA TABLA DEBERÁ TENER 7 FILAS, UNA POR RUBRO (el rubro 72 no tuvo ventas).

*/
Select * from articulos
select * from vendet
select * from vencab
select* from rubros where rubro in (76, 85, 77, 97, 70, 72, 87, 88)

select 
	r.rubro as 'Rubro',
	r.nombre as 'Tipo de Rubro',
	Sum(vt.cantidad * vt.precio) as 'Importe Total'
into 
	TmpVentasAccesorios 
From rubros r
	inner join articulos a on (a.rubro = r.rubro)
	inner join vendet vt on (vt.articulo = a.articulo)  
	inner join vencab vc on (vt.letra = vc.letra and vt.factura = vc.factura)
where
	r.rubro in (76, 85, 77, 97, 70, 72, 87, 88)
	and vc.anulada = 0
group by
	r.rubro,
	r.nombre
order by 1

select * from TmpVentasAccesorios

/*

10. INSERCIÓN MASIVA A TABLA EXISTENTE

Utilizando INSERT..SELECT agregue a la tabla TmpVentasAccesorios las ventas de artículos de los rubros 89 y 99.

Tome como base la consulta del punto anterior.

TABLAS: rubros, vencab, vendet, articulos (para el SELECT). 

SE DEBERÁN INSERTAR 2 FILAS EN LA TABLA.

*/
Insert into TmpVentasAccesorios
select 
	r.rubro as 'Rubro',
	r.nombre as 'Tipo de Rubro',
	Sum(vt.cantidad * vt.precio) as 'Importe Total'
From rubros r
	inner join articulos a on (a.rubro = r.rubro)
	inner join vendet vt on (vt.articulo = a.articulo)  
	inner join vencab vc on (vt.letra = vc.letra and vt.factura = vc.factura)
where
	r.rubro in (89,99)
	and vc.anulada = 0
group by
	r.rubro,
	r.nombre
order by 1

select * from TmpVentasAccesorios

/*

11. ACTUALIZACIÓN MASIVA DE FILAS

Reemplazar con valor 0 (cero) las columnas TERMINALPOSNET y CENTROCOSTO de la tabla SUCURSALES, solamente para aquellas
sucursales que NO estén activas (Activa = 'N').

SE DEBEN ACTUALIZAR 4 FILAS DE LA TABLA SUCURSAL.

*/
select*from sucursales
UPDATE sucursales
SET terminalposnet = 0, centrocosto = 0
where activa = 'N'

/*

12. ELIMINACIÓN MASIVA DE FILAS

Borre de la tabla TmpVentasAccesorios creada en el punto 9 y actualizada en el punto 10, las filas correspondientes a los
rubros que NO superaron los 20.000 en el total de ventas.

SE DEBEN ELIMINAR 4 FILAS DE LA TABLA.

*/
DELETE TmpVentasAccesorios WHERE [Importe Total] <= 20000
select * from TmpVentasAccesorios
 
/*

13. MODIFICACION DE DATOS CON TRANSACCIONES

Implemente en un bloque BEGIN TRANSACTION el borrado de TODAS las filas de la tabla GASTOS (tiene 3 filas).

Verifique si quedó vacía (con 0 filas) y en caso afirmativo haga ROLLBACK para volver a la situación inicial (con 3 filas).

*/
Begin transaction
	DELETE FROM GASTOS
	SELECT * FROM GASTOS
		if @@ROWCOUNT = 0
			Begin
				ROLLBACK TRANSACTION
				Print('Hice el ROLLBACK')
			end
		else
			COMMIT TRANSACTION
			Print('Hice la transaccion')
/*

14. PROCEDIMIENTO ALMACENADO SIMPLE

Cree el procedimiento almacenado "sp_articulos_marca" que retorne solamente la cantidad de artículos perteneciente
a una determinada marca. La marca debe ser solicitada como parámetro de entrada por el procedimiento.

Debe mostrar el mensaje "Existen [cantidad] artículos de la marca [código]."

Ejecute el procedimiento con la marca 'B' para probar. DEBE RETORNAR EL MENSAJE: Existen 1510 artículos de la marca B.

*/
CREATE or ALTER PROCEDURE sp_articulos_marca
	@marca char(1)
AS
DECLARE
	@Cantidad int
BEGIN
	select @Cantidad = Count(articulo) FROM articulos where marca = @marca
	Print('Existen '+ LTRIM(str(@Cantidad)) + ' artículos de la marca ' + @marca)
END

Exec sp_articulos_marca 'a'
	
/*

15. PROCEDIMIENTO ALMACENADO CON MANEJO DE ERRORES

Implemente un procedimiento almacenado que permita insertar nuevos rubros en la tabla correspondiente.

El procedimiento deberá tener el nombre "sp_inserta_rubro", y debe solicitar como parámetros de entrada 
el CODIGO (rubro) y NOMBRE.

Utilice manejo de transacciones para volver atrás la inserción en caso de error.

Se deberá validar la ocurrencia de errores, mostrando los siguientes mensajes:
	- El rubro [código] ya existe en la tabla. (CUANDO SE QUIERA INGRESAR UN RUBRO EXISTENTE).
	- El rubro [nombre] fue dado de alta correctamente. (EN CASO DE ÉXITO)
	- Se produjo un error durante la inserción. (EN CASO DE QUE FALLE LA INSERCIÓN)

Realice dos ejecuciones de prueba, una con un rubro nuevo, y otra con un rubro existente.

*/
SElECT * FROM rubros
CREATE OR ALTER PROCEDURE sp_inserta_rubro
	@codigo int,
	@nombre	char(30)
AS
BEGIN
	IF exists (Select * FROM rubros where rubro = @codigo)
		print('El Rubro ' + trim(str(@codigo)) + ' Ya existe en la tabla')
	ELSE
		BEGIN
			INSERT INTO rubros
				(rubro,nombre)
			VAlUES
				(@codigo,@nombre)
			IF @@ERROR = 0
				PRINT('El rubro ' + ltrim(rtrim(@nombre)) + ' Fue ingresado Correctamente')
			else
				PRINT('Se produjo un error durante la inserción')
		END
END

EXEC sp_inserta_rubro 100,@nombre

DELETE FROM rubros
WHERE rubro IN(100)
/*

16. PROCEDIMIENTO ALMACENADO CON USO DE TRY / CATCH

Implemente el mismo procedimiento anterior, con el mismo comportamiento, pero utilizando para el manejo de errores
los bloques TRY y CATCH.

Realice dos ejecuciones de prueba, una con un rubro nuevo, y otra con un rubro existente.

*/

CREATE OR ALTER PROCEDURE sp_inserta_rubro
	@codigo int,
	@nombre	char(30)
AS
BEGIN TRY 
		BEGIN TRANSACTION 
			INSERT INTO rubros
				(rubro,nombre)
			VAlUES
				(@codigo,@nombre)
		COMMIT TRANSACTION -- CONFIRMA LA INSERCIÓN

		PRINT 'La marca ' + TRIM(@nombre) + ' se insertó correctamente.'
END TRY
BEGIN CATCH
	ROLLBACK TRANSACTION
	IF exists (Select * FROM rubros where rubro = @codigo)
		print('El Rubro ' + trim(str(@codigo)) + ' Ya existe en la tabla')
	ELSE
		PRINT('Se produjo un error durante la inserción')
END CATCH

EXEC sp_inserta_rubro PERO,100

DELETE FROM rubros
WHERE rubro IN(100,1002)