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
-- Actividad 3
BEGIN TRANSACTION 
	UPDATE rubros
		SET nombre = 'VINCHAS'
		WHERE rubro = 52
	INSERT INTO rubros (rubro,nombre)
		VALUES (99,'SKATERS')
	IF @@ERROR = 0
		COMMIT TRANSACTION
	ELSE
		ROLLBACK TRANSACTION
END 

--ACTIVIDAD 4
ALTER PROCEDURE sp_inserta_sucursal
	@codigo int,
	@denominacion char(30),
	@direccion char(30)
AS
BEGIN TRY
	BEGIN TRANSACTION 
		INSERT INTO sucursales (sucursal,denominacion,direccion,Activa)
			VALUES (@codigo,@denominacion,@direccion,'N')
		COMMIT TRANSACTION
		PRINT 'La Nueva Sucursal '+ ltrim(rtrim(@denominacion)) + ' fue dada de alta correctamente'
END TRY
BEGIN CATCH 
	if ERROR_NUMBER() = 2627
		PRINT 'La Sucursal ' + ltrim(rtrim(@denominacion)) + ' ya existe.'
	ELSE
		PRINT 'Hubo un problema! No se pudo insertar la Sucursal.'
END CATCH
-- Para saber cual es la sucursal mas alta
select max(sucursal) from sucursales
-- Ejecuto una instruccion
EXEC sp_inserta_sucursal 101, 'PARQUE BELGRANO', 'PARQUE BELGRANO MANZANA I' 
-- Elimino la sucursal que agrege
delete sucursales where sucursal = 101