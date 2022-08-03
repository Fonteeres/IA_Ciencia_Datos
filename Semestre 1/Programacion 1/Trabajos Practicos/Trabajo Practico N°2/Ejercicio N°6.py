# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:48:48 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°6
Escribir un programa que tome un carácter e informe si es una vocal o no lo es. 
"""

def vocal():
    print('Ingrese una palabra y le digo si es una vocal')
    Palabra = str(input('Ingrese su vocal: '))
    print('')
    if Palabra == 'a' or Palabra == 'e' or Palabra == 'i' or Palabra == 'o' or Palabra == 'u':
        print('Es una vocal')
    else:
        print('la palabra ingresada no es una vocal')
        

vocal()

        