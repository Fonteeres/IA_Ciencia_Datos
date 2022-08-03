# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:52:02 2021

@author: gino_
 Trabajo Practico N°2
 Ejercicio N° 11
Escribir un programa que sume todos los números de una lista de datos.
Por ejemplo [1,3,5] dará como resultado 9. 
"""

A = int(input('Ingresa un numero: '))
B = int(input('Ingresa un numero: '))
C = int(input('Ingresa un numero: '))

lista = [A, B, C]
x = 0

for i in lista:
    x = x + i
print (x)