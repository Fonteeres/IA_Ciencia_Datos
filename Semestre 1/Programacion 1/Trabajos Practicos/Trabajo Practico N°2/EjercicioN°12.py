# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:00:47 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°12
Escribir un programa que multiplique todos los números de una lista de datos.
Por ejemplo [1,2,3] dará como resultado 6.
"""

A = int(input('Ingresa un numero: '))
B = int(input('Ingresa un numero: '))
C = int(input('Ingresa un numero: '))

lista = [A, B, C]
x = 1

for i in lista:
    x = x * i
print (x)