# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:39:10 2021

@author: gino_
Trabajo Practico N°2
Ejercicio 1
Escriba un programa que simule un juego en el que dos jugadores (Álvaro y Bárbara)
tiran un dado. El que saque el valor más alto, gana. Si la puntuación coincide, empatan. 
"""

from random import randint as ran
alvaro= int(ran(1,6))
barbara= int(ran(1,6))

if alvaro > barbara :
    print ('Ganó Alvaro')
elif alvaro == barbara:
    print('Empate')
else:
    print('Ganó Barbara')

