# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:29:25 2021

@author: gino_

Ejemplo: ingreso las medidas de los lados de un triangulo.
El programa debera decir que tipo de triangulo es:
    *Equilatero: Todos sus lados iguales 
    *Escaleno: Todos difernetes
    *Isosceles: 2 iguales y 1 distinto
"""

print ('medidas de los lados de un triangulo')

A = int(input('ingrese lado A: '))
B = int(input('ingrese lado B: '))
C = int(input('ingrese lado C: '))

if A == B and B == C:
    print('Todos los lados son iguales, es Equilatero')
elif (A == B !=C) or (A == C !=B) or (B==C !=A):
    print('Dos lados son iguales y otro no, es Isosceles')
else:
    print ('Todos los lados son diferntes, es Escaleno')



