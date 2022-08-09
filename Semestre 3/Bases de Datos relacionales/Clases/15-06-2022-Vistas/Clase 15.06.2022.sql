/*

VISTAS

*/

CREATE VIEW v_resumen_ventas_articulos AS
SELECT
	md.articulo AS "Código",
	a.nombre AS "Nombre",
	SUM(md.cantidad) AS "Cantidad Vendida",
	'MAY' AS "Tipo Venta"
FROM
	mayordet AS md
	INNER JOIN articulos AS a
	ON md.articulo = a.articulo
	INNER JOIN mayorcab AS mc
	ON mc.letra = md.letra AND mc.factura = md.factura
WHERE
	mc.anulada = 0
GROUP BY
	md.articulo,
	a.nombre
HAVING
	SUM(md.cantidad) > 0
--
UNION
--
SELECT
	vd.articulo,
	a.nombre,
	SUM(vd.cantidad),
	'MIN'
FROM
	vendet AS vd
	INNER JOIN articulos AS a
	ON vd.articulo = a.articulo
	INNER JOIN vencab AS vc
	ON vc.letra = vd.letra AND vc.factura = vd.factura
WHERE
	vc.anulada = 0
GROUP BY
	vd.articulo,
	a.nombre
HAVING
	SUM(vd.cantidad) > 0

SELECT * FROM v_resumen_ventas_articulos

SELECT SUM("Cantidad Vendida") FROM v_resumen_ventas_articulos WHERE "Código" = 'A105210015'

SELECT "Cantidad Vendida" FROM v_resumen_ventas_articulos WHERE "Código" = 'A105210015'

DROP VIEW v_resumen_ventas_articulos

EXEC sp_helptext v_resumen_ventas_articulos