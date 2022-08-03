# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:50:09 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°10
Escribir un programa que muestre una palabra letra por letra. 
"""

def ContadorDePalabras():
    Palabra = str(input('Ingrese su palabra: '))
    for i in Palabra:
        print('Dame una',i)
    print(Palabra)
      
    
ContadorDePalabras()