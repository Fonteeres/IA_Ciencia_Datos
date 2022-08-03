# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:26:12 2021

@author: gino_
Trabajo Practico N°1
Ejercicio 15
15.	Se necesita un programa que tenga la siguiente funcionalidad: 
•	El programa deberá generar dos números aleatorios y mostrarlos en pantalla.
•	También deberá generar aleatoriamente un número comprendido entre 1 y 4. Este número determinará un operación que se deberá mostrar en la pantalla:
o	Cuando se genera un 1, se muestra el signo + (sumar).
o	Cuando se genera un 2, se muestra el signo - (restar).
o	Cuando se genera un 3, se muestra el signo * (multiplicar).
o	Cuando se genera un 4, se muestra el signo / (dividir).
•	El usuario deberá ingresar el resultado de la operación solicitada. Si es el resultado correcto el programa felicitará al usuario, 
    de lo contrario le dirá que se equivocó y le informará el resultado correcto. 

"""

from random import randint as ran
a= int(ran(1,10))
b= int(ran(1,10))
print ("El número generado es: ", str(a))
print ('El numero generado es: ', str(b))
print ('')
print('juguemos a un juego:')
print('Le dire que tiene que hacer con los dos numeros de aqui arriba y si lo hace bien tiene premio')
c= int(ran(4,4))

if c == 1:
    Resultado= a + b
    print('Debe sumar el primer numero por el segundo')
    Usuario = int(input('Ingrese el resultadod de la suma: '))
    if Resultado == Usuario:
        print('Felicidades sabe sumar')
    else: 
        print('Porfavor recursé primaria')
if c == 2:
    Resultado= a - b
    print('Debe restar el primer numero por el segundo')
    Usuario = int(input('Ingrese el resultadod de la resta: '))
    if Resultado == Usuario:
        print('Felicidades sabe restar')
    else: 
        print('Porfavor recursé primaria')
if c == 3:
    Resultado= a * b
    print('Debe multiplicar el primer numero por el segundo')
    Usuario = int(input('Ingrese el resultadod de la multiplicacion: '))
    if Resultado == Usuario:
        print('Felicidades sabe multiplicar')
    else: 
        print('Porfavor recursé primaria')
if c == 4:
    Resultado= int(a / b)
    print('Debe dividir el primer numero por el segundo')
    Usuario = int(input('Ingrese el resultadod de la division: '))
    if Resultado == Usuario:
        print('Felicidades sabe dividir')
    else: 
        print('Porfavor recursé primaria')