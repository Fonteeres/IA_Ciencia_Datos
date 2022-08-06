USE Ventas2

/*

CONSULTA 1: Se crearon algunos artículos en el sistema para realizar pruebas de los distintos procesos. Estos artículos tienen
la palabra PRUEBA dentro de su nombre.

Se desea identificar si se hicieron por error facturas por venta minorista incluyendo esos artículos.

Listar LETRA y FACTURA ordenados de forma ascendente.

*/

SELECT
	letra AS "Letra",
	factura AS "Factura"
FROM 
	vendet 
WHERE 
	articulo IN (SELECT articulo FROM articulos WHERE nombre LIKE '%PRUEBA%')
ORDER BY
	1,2

/*

CONSULTA 2: Se solicita listar las facturas por ventas mayoristas del año 2008, correspondientes a clientes activos (activo = 'A')
que pertenezcan a la provincia de Córdoba (cp que estén entre 5000 y 5999). 

Excluir las facturas cuyo total sea igual o menor a cero, y las ventas anuladas.

Listar: MES, LETRA, FACTURA, TOTAL, DESCUENTO (dto1), Y TOTAL C/DTO (el total de la factura con el descuento aplicado)

Ordenar por mes, letra y factura.

*/

SELECT
	MONTH(fecha) AS "Mes",
	letra AS "Letra",
	factura AS "Factura",
	total AS "Total",
	dto1 AS "Descuento",
	total - ((total*dto1) / 100) AS "Total c/dto"
FROM
	mayorcab
WHERE
	cliente IN (SELECT cliente FROM clientes WHERE estado = 'A' AND cp BETWEEN '5000' AND '5999')
	AND anulada = 0
	AND YEAR(fecha) = 2008
	AND total > 0
ORDER BY
	1,2,3


/*

CONSULTA 3: La empresa quiere dar un premio económico a los vendedores activos (activo = 'S') 
encargados de sucursal (encargado = 'S') que realizaron ventas minoristas en el primer semestre
del año 2006.

Listar sucursal, nombre y antigüedad. Calcular la antigüedad tomando la diferencia entre el año actual
y el año de ingreso del vendedor. Ordenar por sucursal y vendedor.

*/

SELECT
	sucursal AS "Sucursal",
	nombre AS "Vendedor",
	YEAR(GETDATE()) - YEAR(ingreso) AS "Antigüedad"
FROM
	vendedores
WHERE
	encargado = 'S'
	AND activo = 'S'
	AND vendedor IN (SELECT
						DISTINCT vendedor
					FROM
						vencab
					WHERE
						anulada = 0
						AND fecha BETWEEN '2006-01-01' AND '2006-06-30')
ORDER BY
	1, 2