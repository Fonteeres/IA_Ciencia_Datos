# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:04:07 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°14
Escribir un programa que tome un número entero y un carácter, 
y dibuje tantas veces ese carácter como el valor del número indique. 
Por ejemplo: si se ingresa un 5 y una x se debe mostrar xxxxx.
"""

A = int(input('Ingresa un numero: '))
B = int(input('Ingresa un numero: '))
C = int(input('Ingresa un numero: '))
F = str(input('Ingrese el caracter que quiere que se repita: '))

lista = [A, B, C]

print(lista[0] * F)
print(lista[1] * F)
print(lista[2] * F)