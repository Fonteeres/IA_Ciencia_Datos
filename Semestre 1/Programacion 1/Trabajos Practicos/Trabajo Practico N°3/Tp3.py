# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:29:27 2021

@author: gino_
Trabajo Practico N°3
"""

'Funciones'

def Suma():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    print('')
    print('La suma de A y B es de:', A + B)
    
def Resta():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    print('')
    if A > B:
        print('La resta de A y B es de:', A - B)
    else:
        print('La resta de B y A es de:', B - A)
        
def Multiplicacion():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    print('La Multiplicacion de A y B es de:', B * A)
    
def Max():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    print('')
    if A > B:
        print('A es mayor que B')
    elif B > A:
        print('B es mayor que A')
    else:
        print('Ambos son iguales')
        
def Min():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    print('')
    if A > B:
        print('B es menor que A')
    elif B > A:
        print('A es menor que B')
    else:
        print('Ambos son iguales')
        
def Max_de_tres():
    A = int(input('Ingrese el Numero A: '))
    B = int(input('Ingrese el Numero B: '))
    C = int(input('Ingrese el Numero C: '))
    print('')
    if A > B and A > C:
        print('A es mayor que B y C')
    elif B > A and B > C:
        print('B es mayor que A y C')
    elif C > A and C > A:
        print('C es mayor que A y B')
    else:
        print('Todos son iguales')
        
def Vocal():
    print('Ingrese una palabra y le digo si es una vocal')
    Palabra = str(input('Ingrese su vocal: '))
    print('')
    if Palabra == 'a' or Palabra == 'e' or Palabra == 'i' or Palabra == 'o' or Palabra == 'u':
        print('True')
    else:
        print('False')
        
def Inversa(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    print(palabra_invertida)
    
def Es_palindromo(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    print(palabra_invertida)
    
def long():
    A = str(input('Ingrese la palabra: '))
    x = 0
    for i in A:
        x = x + 1
    print('Len = ', x)

def Superposicion():
    A = str(input('Ingresa una palabra: '))
    B = str(input('Ingresa una palabra: '))
    C = str(input('Ingresa una palabra: '))
    D = str(input('Ingresa una palabra: '))
    E = str(input('Ingresa una palabra: '))
    F = str(input('Ingresa una palabra: '))
    
    lista1 = [A, B, C]
    lista2 = [D, E, F]
    
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                print( 'True')
            else:
                print('False')
def Generar_n_caracteres():
    A = int(input('Ingresar la cantidad de Caracteres: '))
    B = str(input('Ingresar el Caracter: '))
    
    print(A * B)    
    
    
    

'Ejecucion de las Funciones'
print('Elija el programa a ejecutar')
print('1: Suma')
print('2: Resta')
print('3: Multiplicacion')
print('4: Determinar el Mas Grande')
print('5: Determinar el Mas chico')
print('6: Determinar el Mas grande pero con 3 valores')
print('7: Determinar si el caracter ingresado es una vocal')
print('8: Dar vuelta una palabra')
print('9: Identificar palíndromos')
print('10: Calcular la longitud de un texto')
print('11: Determinar si hay un miembro en comun en unos texto')
print('12: Ingresar un valor numerico y devuelva la misma cantidad de letras')
print('13: Salir')

Eleccion= int(input("escriba la operacion que desea realizar: "))
while Eleccion != 13:
    if Eleccion==1:
        Suma()
    
    elif Eleccion==2:
        Resta()
        
    elif Eleccion==3:
        Multiplicacion()
    
    elif Eleccion==4:
        Max()
        
    elif Eleccion==5:
        Min()
    
    elif Eleccion==6:
        Max_de_tres()
    
    elif Eleccion==7:
        Vocal()
    
    elif Eleccion==8:
        Inversa()
    
    elif Eleccion==9:
        Es_palindromo()
    
    elif Eleccion==10:
        long()
    
    elif Eleccion==11:
        Superposicion()
        
    elif Eleccion==12:
        Generar_n_caracteres()
    
    else:  
        print("datos ingresados incorrectamente")
    print('Elija el programa a ejecutar')
    print('1: Suma')
    print('2: Resta')
    print('3: Multiplicacion')
    print('4: Determinar el Mas Grande')
    print('5: Determinar el Mas chico')
    print('6: Determinar el Mas grande pero con 3 valores')
    print('7: Determinar si el caracter ingresado es una vocal')
    print('8: Dar vuelta una palabra')
    print('9: Identificar palíndromos')
    print('10: Calcular la longitud de un texto')
    print('11: Determinar si hay un miembro en comun en unos texto')
    print('12: Ingresar un valor numerico y devuelva la misma cantidad de letras')
    print('13: Salir')

    Eleccion= int(input("escriba la operacion que desea realizar: "))
    
    