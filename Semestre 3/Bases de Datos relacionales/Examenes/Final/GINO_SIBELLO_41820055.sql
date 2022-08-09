-- Actividad 1
/*
Actividad 1 (35 puntos): Determinar los 10 mejores clientes mayoristas del segundo semestre del año 2007, presentando un ranking 
decreciente por importe total comprado. Incluir solamente aquellos clientes que compraron más de 500 prendas y superaron los 20.000 
pesos. Presentar: CLIENTE, NOMBRE, CANTIDAD DE PRENDAS, IMPORTE TOTAL. Excluya las facturas anuladas (las facturas anuladas tienen 
el valor 1 en la columna ANULADA), incluya solamente los clientes activos (tienen el valor ‘A’ en la columna ESTADO) y 
calcule el importe total utilizando CANTIDAD * PRECIOREAL.
*/
SELECT TOP 10
	c.cliente,
	c.nombre,
	sum(md.cantidad) as 'Cantidad de Prendas',
	sum(md.cantidad * md.precioreal) as 'Importe Total'
FROM mayordet md
	inner join mayorcab mc on (mc.letra = md.letra and mc.factura = md.factura)
	inner join clientes c on (mc.cliente = c.cliente)
WHERE
	mc.anulada = 0
	and c.estado = 'A'
	and mc.fecha between '01/06/2007' and '31/12/2007'
GROUP BY
	c.cliente,
	c.nombre
HAVING
	sum(md.cantidad) > 500 and
	sum(md.cantidad * md.precioreal) > 20000
ORDER BY
	4 desc
/*
Actividad 2 (30 puntos): Cuando la empresa comenzó su actividad, compró 500 unidades del artículo A208220085 (JEAN MAR). 
Se le solicita determinar la cantidad de unidades que quedan actualmente, teniendo en cuenta las cantidades vendidas hasta 
ahora en forma mayorista y minorista (excluyendo facturas anuladas en ambos casos). Si bien se puede resolver en una sola instrucción,
puede utilizar los recursos que considere pertinentes para determinar esta cantidad.
*/
--Actividad 2
SELECT
	Count(vd.factura) as 'TOTAL'
FROM articulos a
	inner join vendet vd on (a.articulo = vd.articulo)
	inner join vencab vc on (vc.factura = vd.factura and vc.letra = vd.letra)
WHERE 
	a.articulo = 'A208220085'
	and vc.anulada = 0
		
	UNION
	
SELECT
	Count(md.factura) as 'TOTAL'
FROM articulos a
	inner join mayordet md on (md.articulo = a.articulo)
	inner join mayorcab mc on (mc.letra = md.letra and mc.factura = md.factura)
WHERE
	a.articulo = 'A208220085'
	and mc.anulada = 0


/*
Actividad 3 (35 puntos): Crear el procedimiento almacenado sp_articulos_sin_ventas que, recibiendo como parámetro un año determinado, 
cree la tabla TmpArticulosSinVentas. Esta tabla deberá contener los artículos que no registraron ninguna venta minorista en el año 
especificado. Se consideran artículos sin ventas aquellos que no fueron incluidos en una factura durante ese año. La estructura de 
la tabla debe ser: CÓDIGO (articulo), NOMBRE, PRECIOMAYOR y PRECIOMENOR. El procedimiento deberá validar la existencia de la tabla 
y contar con manejo de errores y mensajes con el resumen de la cantidad de filas insertadas.
*/
CREATE PROCEDURE sp_articulos_sin_ventas
	@Año int
As
BEGIN TRY
	IF OBJECT_ID('TmpArticulosSinVentas') is null
			CREATE TABLE TmpArticulosSinVentas (
				Articulo char(20),
				Nombre char(40),
				PrecioMayor decimal(9,2),
				PrecioMenor decimal(9,2))
	ELSE 
		TRUNCATE TABLE TmpArticulosSinVentas

	BEGIN TRANSACTION 
		INSERT INTO TmpArticulosSinVentas
		SELECT 
			articulo,
			nombre,
			preciomenor,
			preciomayor
		FROM articulos
		WHERE
			 articulo not in (SELECT vd.articulo FROM vencab vc inner join vendet vd on(vc.letra = vd.letra and vc.factura = vd.factura) WHERE year(fecha) = @Año)

	PRINT 'Las tablas Afectas Son ' + rtrim(ltrim(str(@@rowcount)))

	COMMIT TRANSACTION
END TRY
BEGIN CATCH 
	ROLLBACK TRANSACTION 
	
	PRINT 'HUBO UN ERROR COMUNIQUESE CON SU ADMINISTRADOR'
END CATCH

EXEC sp_articulos_sin_ventas 2007

select * from TmpArticulosSinVentas

DROP TABLE TmpArticulosSinVentas