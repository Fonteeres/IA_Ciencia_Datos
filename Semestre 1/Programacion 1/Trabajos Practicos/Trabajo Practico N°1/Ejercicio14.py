# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:05:39 2021

@author: gino_
Trabajo Practico N°1
Ejercicio 14
14.	Se necesita un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
"""

print('Ingrese dos Numeros')
Numero1 = int(input('Numero 1: '))
Numero2 = int(input('Numero 2: '))

if Numero1 > Numero2:
    print(Numero1,'es mas grande que', Numero2)
    Multiplos = Numero1 % Numero2
    if Multiplos == 0:
        print(Numero1,'Es multiplo de ', Numero2 )
    else:
        print(Numero1, 'No es multiplo de ', Numero2)
if Numero1 < Numero2:
    print(Numero2,'es mas grande que', Numero1)
    Multiplos = Numero2 % Numero1
    if Multiplos == 0:
        print(Numero2,'Es multiplo de ', Numero1 )
    else:
        print(Numero2, 'No es multiplo de ', Numero1)
    