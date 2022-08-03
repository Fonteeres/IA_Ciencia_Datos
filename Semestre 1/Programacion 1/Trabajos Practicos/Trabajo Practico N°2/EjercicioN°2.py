# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:49:00 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°2
Escriba un programa que simule un juego en el que dos jugadores (Carmen y David)
tiran dos dados. El que saque mayor puntuación total, gana. Si la puntuación 
total coincide, gana quien haya sacado el dado con el valor más alto. 
Si el valor más alto también coincide, empatan. 
"""

from random import randint as ran
c = 0
d = 0
em = 0
i = 0

while i <= 20:
    carmen = int(ran(1,6))
    david = int(ran(1,6))
    if carmen > david:
        c = c + 1 
    elif david > carmen:
        d = d + 1
    else:
        em = em +1 ## Es solo para saber las veces que empataron
    i = i + 1
    
if c > d :
    print('Ganó Carmen')
elif d > c:
    print('Ganó David')
elif c == d:
    if carmen > david :
        print('Ganó Carmen')
    elif carmen < david :
        print('Gano David')
    else:
        print('Empate')
     
                            