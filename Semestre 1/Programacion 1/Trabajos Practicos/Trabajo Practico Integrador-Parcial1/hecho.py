# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:55:24 2021

@author: gino_
Trabajo Practico Integrador
Pre-Parcial
"""
def DescubrirMenor():
    A = int(input('Ingresar el Primer Numero: '))
    B = int(input('Ingresar el Segundo Numero: '))
    C = int(input('Ingresar el Tercer Numero: '))
    
    if A < B and A < C :
        print(A,'Es menor que',B ,'y', C)
    elif B < A and B < C:
        print(B,'Es menor que',A,'y',C)
    elif C < A and C < A:
        print(C,'Es menor que',A ,'y',B)
    else:
        print('Los tres son Iguales')
    
    
def TipoDeTriangulo():
    A = int(input('Ingresar el Primer Angulo: '))
    B = int(input('Ingresar el Segundo Angulo: '))
    C = int(input('Ingresar el Tercer Angulo: '))
    
    Prueba = A + B + C
    
    if Prueba == 180 :
        if A > 90 or B > 90 or C > 90:
            print('Es un triangulo obtusangulo')
        elif A == 90 or B == 90 or C == 90:
            print('Es un triangulo Rectangulo')
        elif A < 90 or B < 90 or C < 90:
            print('Es un triangulo Acutangulo')
    else: 
        print('Los angulos dados no corresponden a los de un triangulo')
        
def ContarVocales():
    A = str(input('Ingrese una palabra o una oracion: '))
    A_lower = A.lower()
    x = 0
    for i in A_lower:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            x = x + 1
    if x == 0:
        print('La palabra o oracion dada no tiene vocales')
    else:
        print('La palabra o oracion dada tiene', x,'Vocales')
    
def EsPalindromo():
    A = str(input('Ingrese la Palabra:  '))
    print('')
    Palabra_invertida = ''
    for i in A:
        Palabra_invertida = i + Palabra_invertida
    if Palabra_invertida == A:
        print (Palabra_invertida,'es igual a ', A)
        print('Por ende Es un palabra palindroma')
    else:
        print(Palabra_invertida,'No es igual a ', A)
        

    
