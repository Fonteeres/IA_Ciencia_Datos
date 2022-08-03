# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:04:11 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°15
Escribir un programa que dibuje un histograma tomando los datos de una lista de números enteros. 
Por  ejemplo: si la lista tiene los siguientes datos: [4, 9, 7]) el programa debería imprimir lo siguiente: 
**** 
********* 
******* 
"""

A = int(input('Ingresa un numero: '))
B = int(input('Ingresa un numero: '))
C = int(input('Ingresa un numero: '))
print('')

lista = [A, B, C]

print(lista[0] * '*')
print(lista[1] * '*')
print(lista[2] * '*')