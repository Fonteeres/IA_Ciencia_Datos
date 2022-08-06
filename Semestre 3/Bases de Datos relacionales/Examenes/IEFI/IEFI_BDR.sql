/*

PUNTO 1

Desarrolle una consulta que presente Artículo, Nombre, Total y TipoVenta (esta última columna es un LITERAL, y sus valores
pueden ser ‘Mayorista’ o ‘Minorista’). Debe listar aquellos artículos que vendieron un mínimo de ventas de $5000 en cualquiera
de los tipos de venta en el año 2006. Utilice para resolver la cláusula UNION ALL. Excluya siempre las ventas anuladas, y tome
para el cálculo del total “cantidad * precio” para ventas minoristas, y “cantidad * precioreal” para ventas mayoristas. 

TABLAS: articulos, mayorcab y mayordet (conjunto 1); articulos, vencab, vendet (conjunto 2). 

*/

SELECT
	a.articulo as Articulo,
	a.nombre as Nombre,
	sum(vd.cantidad * vd.precio) as Total,
	'Menor' as TipoVenta
from
	vencab as vc
	inner join vendet as vd
	on vc.letra = vd.letra and vc.factura = vd.factura
	inner join articulos as a
	on vd.articulo = a.articulo
where
	year(vc.fecha) = 2006
	and vc.anulada = 0
group by
	a.articulo,
	a.nombre
having
	sum(vd.cantidad * vd.precio) > 5000
--
UNION ALL
--
SELECT
	a.articulo as Articulo,
	a.nombre as Nombre,
	sum(md.cantidad * md.precioreal) as Total,
	'Mayor' as TipoVenta
from
	mayorcab as mc
	inner join mayordet as md
	on mc.letra = md.letra and mc.factura = md.factura
	inner join articulos as a
	on md.articulo = a.articulo
where
	year(mc.fecha) = 2006
	and mc.anulada = 0
group by
	a.articulo,
	a.nombre
having
	sum(md.cantidad * md.precioreal) > 5000

/*

PUNTO 2

Cree un SP basado en la consulta anterior que genere la tabla TmpComparativoVentas que tenga la misma estructura de la consulta,
pero que solicite como parámetros de entrada el Año (2006 en el ejercicio anterior) y el Mínimo de ventas (5000 en el ejercicio
anterior). Tenga en cuenta:
- Valide la existencia de la tabla antes de crearla o truncarla. Para crearla en caso de que corresponda hacerlo, utilice la siguiente instrucción dentro del procedimiento:
		
		CREATE TABLE TmpComparativoVentas (
		Articulo char(10),
		Nombre char(40),
		Total decimal(9,2),
		TipoVenta char(10))

- Valide la ocurrencia de errores durante la inserción.
- Muestre al final de la ejecución un mensaje con la cantidad de filas insertadas.
- Presente al final las sentencias de ejecución del procedimiento y una consulta sobre la tabla creada para verificar su corrección.


*/

CREATE OR ALTER PROCEDURE sp_ComparativoVentas
	@a int,
	@m decimal (9,2)
AS
BEGIN TRY
	-- VALIDA LA EXISTENCIA DE LA TABLA
	IF OBJECT_ID('TmpComparativoVentas') IS NULL
		CREATE TABLE TmpComparativoVentas(
		Articulo char(10),
		Nombre char(40),
		Total decimal(9,2),
		TipoVenta char(10))	
	ELSE
		TRUNCATE TABLE TmpComparativoVentas
	--
	BEGIN TRANSACTION
	--
	INSERT INTO TmpComparativoVentas
	SELECT
		a.articulo as Articulo,
		a.nombre as Nombre,
		sum(vd.cantidad * vd.precio) as Total,
		'Menor' as TipoVenta
	from
		vencab as vc
		inner join vendet as vd
		on vc.letra = vd.letra and vc.factura = vd.factura
		inner join articulos as a
		on vd.articulo = a.articulo
	where
		year(vc.fecha) = @a
		and vc.anulada = 0
	group by
		a.articulo,
		a.nombre
	having
		sum(vd.cantidad * vd.precio) > @m
	--
	UNION ALL
	--
	SELECT
		a.articulo as Articulo,
		a.nombre as Nombre,
		sum(md.cantidad * md.precioreal) as Total,
		'Mayor' as TipoVenta
	from
		mayorcab as mc
		inner join mayordet as md
		on mc.letra = md.letra and mc.factura = md.factura
		inner join articulos as a
		on md.articulo = a.articulo
	where
		year(mc.fecha) = @a
		and mc.anulada = 0
	group by
		a.articulo,
		a.nombre
	having
		sum(md.cantidad * md.precioreal) > @m
	--
	PRINT 'Se insertaron ' + TRIM(STR(@@ROWCOUNT)) + ' filas.'
	--
	COMMIT TRANSACTION
END TRY

BEGIN CATCH

	ROLLBACK TRANSACTION
	--
	PRINT 'Se produjeron errores durante la inserción en la tabla TmpComparativoVentas.'

END CATCH

exec sp_ComparativoVentas 2005, 20000

SELECT * FROM TmpComparativoVentas

DROP TABLE TmpComparativoVentas

SELECT OBJECT_ID('TmpComparativoVentas')