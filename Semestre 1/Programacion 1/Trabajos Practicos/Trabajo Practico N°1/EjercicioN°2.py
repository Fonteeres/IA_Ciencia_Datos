# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:43:17 2021

@author: gino_
Trabajo Practico N°1
Ejercicio N°2.
Se necesita un programa que tenga la siguiente funcionalidad: 
el usuario debe ingresar dos números, el programa debe indicar 
cuál es el mayor.
"""
print('Buenas! que tal extraño?, Ahora estaria necesitando ')
print('que me pongas dos numeros el que quieras asi puedo practicar')
Numero1 = float(input('Ingrese el Primer numero: '))
Numero2 = float(input('Ingrese el Segundo numero: '))

if Numero1 > Numero2:
    print (Numero1,' Es mayor que ', Numero2)
elif Numero2 > Numero1: 
    print(Numero2, ' Es mayor que ', Numero1)
else:
    print('Ambos Numeros son iguales', Numero1 ,'=', Numero2)
