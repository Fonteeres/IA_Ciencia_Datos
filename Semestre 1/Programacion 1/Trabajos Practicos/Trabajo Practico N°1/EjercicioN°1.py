# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:13:09 2021

@author: gino_
Trabajo Practico N°1
Ejercicio 1.	
Se necesita un programa que tenga la siguiente funcionalidad: 
el usuario debe ingresar el precio de un producto y se deberá informar cual 
es el valor del IVA de un producto y su precio final.
"""

producto = float(input('Ingresa el precio de tu producto: '))
B = str(input('¿El producto tiene el IVA? [y/n]:  '))

if B == 'y':
    ValorNeto = producto * 0.1735537190082645
    """
    La razon del 0.173553 es porque si hacemos la igualdad de un producto
    con iva al mismo producto sin el iva, con un pasaje de terminos 
    llegamos a ese numero
    """
    ProductoSinIva = producto - ValorNeto
    print('El iva que tiene tu producyo es ',ValorNeto)
    print('El precio de tu producto sin iva es de ', ProductoSinIva )
else:
    ValorNeto = producto * 0.21
    ProductoConIva = producto + ValorNeto
    print('El Iva en tu producto seria de: ', ValorNeto)
    print('Tu Producto mas el iva seria', ProductoConIva)
   
        