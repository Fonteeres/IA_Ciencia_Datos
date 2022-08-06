USE Ventas2

/*

CONSULTA 1: Se crearon algunos art�culos en el sistema para realizar pruebas de los distintos procesos. Estos art�culos tienen
la palabra PRUEBA dentro de su nombre.

Se desea identificar si se hicieron por error facturas por venta minorista incluyendo esos art�culos.

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

CONSULTA 2: Se solicita listar las facturas por ventas mayoristas del a�o 2008, correspondientes a clientes activos (activo = 'A')
que pertenezcan a la provincia de C�rdoba (cp que est�n entre 5000 y 5999). 

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

CONSULTA 3: La empresa quiere dar un premio econ�mico a los vendedores activos (activo = 'S') 
encargados de sucursal (encargado = 'S') que realizaron ventas minoristas en el primer semestre
del a�o 2006.

Listar sucursal, nombre y antig�edad. Calcular la antig�edad tomando la diferencia entre el a�o actual
y el a�o de ingreso del vendedor. Ordenar por sucursal y vendedor.

*/

SELECT
	sucursal AS "Sucursal",
	nombre AS "Vendedor",
	YEAR(GETDATE()) - YEAR(ingreso) AS "Antig�edad"
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