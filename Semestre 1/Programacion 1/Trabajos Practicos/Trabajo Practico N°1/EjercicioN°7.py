# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:51:37 2021

@author: gino_
Trabajo Practico N°1
Ejercico N°7
Se necesita un programa que tenga la siguiente funcionalidad: el usuario 
debe ingresar las tres medidas de los ángulos de un triángulo, el programa 
deberá verificar que corresponden a un triángulo. Para eso la suma de los 
tres ángulos debe ser igual a 180 grados.
"""
print('Ingresa tres angulos de un triangulo')
print('La suma de las medidas de los tres ángulos internos de un triángulo siempre es 180°')
Angulo1 = int(input('Ingresa el primer Angulo: '))
Angulo2 = int(input('Ingresa el segundo Angulo: '))
Angulo3 = int(input('Ingresa el tercer Angulo: '))

Triangulo = Angulo1 + Angulo2 + Angulo3

if Triangulo == 180:
    print('Los angulos pertenecen a los de un triangulo')
else:
    print('Estos angulos no pertenecen a un triangulo')
