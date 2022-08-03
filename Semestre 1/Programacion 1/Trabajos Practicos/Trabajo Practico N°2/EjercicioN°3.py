# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:23:35 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°3
 
Escriba un programa que simule el juego piedra, papel, tijera para dos jugadores
(Maria y Juan). 
Las reglas del juego son las siguientes: 
Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones: 

El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera. 

El jugador que ha sacado Tijera gana al jugador que ha sacado Papel. 

El jugador que ha sacado Papel gana al jugador que ha sacado Piedra. 

Resuelva este ejercicio utilizando la función randint(), de manera que el 
valor 1 corresponda a Piedra, el valor 2 corresponda a papel y el valor 3 
corresponda a Tijera. 

"""

from random import randint as ran
i = 0
m = 0
j = 0
em = 0

while i <= 50:
    maria = int(ran(1,3))
    juan = int(ran(1,3))
    if maria == 1 and juan == 3:
        m = m + 1
    elif maria == 1 and juan == 2:
        j = j + 1
    elif maria == 2 and juan == 1:
        m = m + 1
    elif maria == 2 and juan == 3:
        j = j + 1
    elif maria == 3 and juan == 1:
        j = j + 1 
    elif maria == 3 and juan == 2:
        m = m + 1 
    else: 
        em = em + 1 # para saber cuanto empataron 
    i = i + 1
    
if m > j :
    print ('Ganó Maria')
elif j > m:
    print('Ganó Juan')
else:
    print('Empate')
        