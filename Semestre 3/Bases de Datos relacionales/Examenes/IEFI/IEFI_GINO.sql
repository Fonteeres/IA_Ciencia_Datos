-- EJERCICIO 1
SELECT 
	a.articulo,
	a.nombre,
	sum(md.cantidad * md.precioreal) as 'Total',
	'May' as 'TipoVenta'
FROM mayorcab  mc
	inner join mayordet md on (mc.letra = md.letra and mc.factura = md.factura)
	inner join articulos a on a.articulo = md.articulo
WHERE
	year(mc.fecha) = 2006
GROUP BY
	a.articulo,
	a.nombre
HAVING
	sum(md.cantidad * md.precioreal) > 5000

UNION ALL 

SELECT 
	a.articulo,
	a.nombre,
	sum(vt.cantidad * vt.precio) as 'Total',
	'Min' as 'TipoVenta'
FROM vencab vc
	inner join vendet vt on (vc.letra = vt.letra and vc.factura = vt.factura)
	inner join articulos a on a.articulo = vt.articulo
WHERE
	year(vc.fecha) = 2006
GROUP BY
	a.articulo,
	a.nombre
HAVING
	sum(vt.cantidad * vt.precio) > 5000

-- EJERCICIO 2

CREATE PROCEDURE  sp_comparativo_ventas
	@Año int,
	@minimoVentas int
AS
BEGIN TRY
	IF object_id('TmpComparativoVentas') is null
		CREATE TABLE TmpComparativoVentas (
							Articulo char(10),
							Nombre char(40),
							Total decimal(9,2),
							TipoVenta char(10))
	ELSE
		TRUNCATE TABLE TmpComparativoVentas

	BEGIN TRANSACTION
		INSERT INTO TmpComparativoVentas
		SELECT 
			a.articulo,
			a.nombre,
			sum(md.cantidad * md.precioreal) as 'Total',
			'May' as 'TipoVenta'
		FROM mayorcab  mc
			inner join mayordet md on (mc.letra = md.letra and mc.factura = md.factura)
			inner join articulos a on a.articulo = md.articulo
		WHERE
			year(mc.fecha) = @Año
			and mc.anulada = 0
		GROUP BY
			a.articulo,
			a.nombre
		HAVING
			sum(md.cantidad * md.precioreal) > @minimoVentas

		UNION ALL 

		SELECT 
			a.articulo,
			a.nombre,
			sum(vt.cantidad * vt.precio) as 'Total',
			'Min' as 'TipoVenta'
		FROM vencab vc
			inner join vendet vt on (vc.letra = vt.letra and vc.factura = vt.factura)
			inner join articulos a on a.articulo = vt.articulo
		WHERE
			year(vc.fecha) = @Año
			and vc.anulada = 0
		GROUP BY
			a.articulo,
			a.nombre
		HAVING
			sum(vt.cantidad * vt.precio) > @minimoVentas

		PRINT 'Se insertaron ' + TRIM(STR(@@ROWCOUNT)) + ' filas.'

		COMMIT TRANSACTION
END TRY
BEGIN CATCH

	ROLLBACK TRANSACTION
	--
	PRINT 'Se produjeron errores durante la inserción en la tabla TmpComparativoVentas.'

END CATCH

exec sp_comparativo_ventas 2005, 20000

SELECT * FROM TmpComparativoVentas

DROP TABLE TmpComparativoVentas

SELECT OBJECT_ID('TmpComparativoVentas')