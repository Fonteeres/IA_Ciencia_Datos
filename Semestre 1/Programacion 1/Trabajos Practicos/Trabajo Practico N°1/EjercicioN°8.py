# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:58:35 2021

@author: gino_
Trabajo Practico N°1
Ejercicio N°8
Se necesita un programa que tenga la siguiente funcionalidad: el usuario 
debe ingresar las tres medidas de los ángulos de un triángulo, el programa 
deberá informar si es obtusángulo, para lo que es necesario verificar si 
uno de los ángulos es mayor a 90 grados.
"""

print('Ingresa tres angulos de un triangulo')
print('La suma de las medidas de los tres ángulos internos de un triángulo siempre es 180°')
print('Tambien si un angulo de los 3 es mayor a 90 grados serie un triangulo obtusangulo')
Angulo1 = int(input('Ingresa el primer Angulo: '))
Angulo2 = int(input('Ingresa el segundo Angulo: '))
Angulo3 = int(input('Ingresa el tercer Angulo: '))

Triangulo = Angulo1 + Angulo2 + Angulo3

if Triangulo == 180:
    if Angulo1>90 or Angulo2>90 or Angulo3>90:
        print('Este triangulo es un obtusangulo')
elif Triangulo > 180:
    print('Los angulos dados no son de un triangulo')



