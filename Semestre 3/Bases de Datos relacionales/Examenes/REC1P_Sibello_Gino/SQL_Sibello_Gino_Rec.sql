--- Actividad 1
select 
	mc.letra,
	mc.factura,
	mc.fecha,
	md.articulo,
	a.nombre,
	md.precioreal,
	md.cantidad
from mayorcab mc
	inner join mayordet md on (mc.letra = md.letra and mc.factura = md.factura)
	inner join articulos a on (md.articulo = a.articulo)
	inner join marcas m on (m.marca = a.marca)
where
	m.marca = 'G' 
	and mc.fecha between '2008/01/01' and '2008/03/31'
	and mc.anulada = 0
order by
	3,4

--- Actividad 2
select
	s.denominacion,
	count(vc.factura) as 'CANTIDAD DE VENTAS',
	sum(vc.total) as 'IMPORTE DE VENTAS',
	sum(vc.total*0.03) as 'PREMIO'
From vencab vc
	inner join sucursales s on (s.sucursal = vc.sucursal)
where
	vc.anulada = 0
	and s.Activa = 'S'
	and year(vc.fecha) = 2007
group by
	s.denominacion
HAVING
	sum(vc.total) > 1000000