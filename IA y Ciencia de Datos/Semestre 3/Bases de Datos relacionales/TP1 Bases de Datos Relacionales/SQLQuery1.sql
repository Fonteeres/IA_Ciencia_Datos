select * from vencab
select * from vendet
select * from vendedores where activo = 'S'
-- ventas de cada vendedor por año
SELECT 
	YEAR(vc.fecha) as Año,
	COUNT(vc.factura) as Total
FROM
	vencab vc
	inner join vendedores v on (v.vendedor = vc.vendedor)
	inner join vendet vt on (vc.letra = vt.letra and vc.factura = vt.factura)
WHERE
	vc.anulada = 0
	and v.vendedor = 3
GROUP BY
	YEAR(vc.fecha)
Order by
	1
--Ventas de sucursales para selecionar
SELECT * FROM sucursales
SELECT * FROM articulos
select * from vencab
select * from vendet
--Ventas de sucursales para selecionar
SELECT
	s.sucursal,
	YEAR(vc.fecha) as Año,
	COUNT(vc.factura) as 'Total Ventas'
FROM vendet vt
	inner join vencab vc on (vt.letra = vc.letra and vt.factura = vc.factura)
	inner join sucursales s on (vc.sucursal = s.sucursal )
WHERE
	vc.anulada = 0
	and s.sucursal = 2
GROUP BY
	s.sucursal,
	YEAR(vc.fecha)
ORDER BY
	1,2
-- Ventas por marca 
SELECT * FROM articulos
Select * from vencab
Select * from vendet
Select * FROM marcas
-- Ventas por marca 
SELECT
	m.marca,
	m.nombre,
	YEAR(vc.fecha),
	COUNT(vc.factura) as 'Total Venta'
FROM articulos a
	inner join marcas m on (m.marca = a.marca)
	inner join vendet vt on (vt.articulo = a.articulo)
	inner join vencab vc on (vc.letra = vt.letra and vc.factura = vt.factura)
WHERE
	vc.anulada = 0
	and m.marca = 'b'
GROUP BY
	m.marca,
	m.nombre,
	YEAR(vc.fecha)
Order by
	1,2