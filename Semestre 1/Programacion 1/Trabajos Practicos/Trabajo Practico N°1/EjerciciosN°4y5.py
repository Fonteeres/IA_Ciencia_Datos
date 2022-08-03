# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:04:00 2021

@author: gino_
Trabajo Practico N°1
Ejercicios N°4 y 5
Se necesita un programa que tenga la siguiente funcionalidad: el usuario 
debe ingresar un número entero y el programa debe informar si está 
comprendido entre 0 y 10, si esta entre 11 y 20, si esta entre 21 y 30 
otro mensaje, o si es mayor a 30.
"""

print('alooooooooo, podria ingresar por favor el nro que usted desee')

NumeroUsuario = float(input('Ingrese su numero aqui por favor: '))

if NumeroUsuario <= 10 and NumeroUsuario >= 0:
    print ('Su Numero esta comprendido entre 0 y 10')
elif NumeroUsuario <= 20 and NumeroUsuario >= 11: 
    print ('Su Numero esta comprendido entre 11 y 20')
elif NumeroUsuario <= 30 and NumeroUsuario >= 21:
    print ('Su Numero esta comprendido entre 21 y 30')
else: 
    print ('Su Numero es Mayor a 30')
    
