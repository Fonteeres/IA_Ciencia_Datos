# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:07:48 2021

@author: Gino Sibello

Profe me queme la cabeza pensando como hacer para que elija preguntas al azar y tambien para que el programa 
deje de andar una vez que el contador llege a donde esta marcado pero no se que le pasa.
"""
from random import randint as ran
def consigna1():
    Archivo = open('Preguntas.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    win = 0
    lose = 0
    a = ran(0,88)
    
    while win < 5 or lose < 3:
        for a in DatosArchivados:
            a = a.replace('\n', '')
            dato = a.split(';')
            print ('pregunta: ' + dato[0])
            print('Respuestas: ')
            print('A: ' + dato[1] + '  B: ' + dato[2] + '  C: ' + dato[3] + '  D: ' + dato[4])
            Respuesta = str(input('Ingrese la respuesta correcta: '))
            if Respuesta == str(dato[5]):
                win = win + 1 
            else:
                lose = lose + 1 
            print(win)
            print(lose)
    if lose == 3:
        print('Perdiste, quieres intententarlo de nuevo?')
    elif win == 5:
        print('Ganaste!, quieres seguir jugando?')
    
        
        
consigna1()