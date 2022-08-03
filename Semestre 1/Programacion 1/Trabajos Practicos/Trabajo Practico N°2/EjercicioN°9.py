# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:13:34 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°9
Escribir un programa que cuente la cantidad de letras de una palabra.  
"""

def ContadorDePalabras():
    Palabra = str(input('Ingrese su palabra: '))
    Contador = 0
    for i in Palabra:
        Contador = Contador + 1
    print(Contador)
      
    
ContadorDePalabras()