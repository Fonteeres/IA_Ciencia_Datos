# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:48:41 2021

@author: gino_
Trabajo Practico N°2
Ejercicio N°4 y Ejercicio N°5
Escribir un programa que tome dos números y devuelva el mayor de ellos.  
Escribir un programa que tome tres números y devuelva el mayor de ellos.  
"""
print('Elija cual modo de juego quiere jugar')
print(' 1- Usamos 2 Numeros 2- Usamos 3 Numeros')
e =int(input('Ingrese su eleccion: '))



if e == 1:
    a = int(input('Ingrese un Numero A: '))
    b = int(input('Ingrese un Numero B: '))
    print('')
    if a > b :
        print(a,'es mayor que',b)
    elif a < b:
        print(b, 'es mayo que', a)
    else:
        print('Son iguales')
elif e == 2:
    a = int(input('Ingrese un Numero A: '))
    b = int(input('Ingrese un Numero B: '))
    c = int(input('Ingrese un Numero C: '))
    print('')
    if a > b and a > c:
        print(a,'es mayor que ', b ,'y', c)
    elif b > a and b > c:
        print(b,'es mayor que', a ,'y',c)
    elif c > a and c > b:
        print (c,'es mayor que', a ,'y',b)
    elif a == b and a > c :
        print(a, 'y',b ,'son mayores que', c)
    elif a == c and a > b:
        print(a, 'y',c ,'son mayores que', b)
    elif b == c and b > a:
        print(b,'y',c,'son mayores que', a)
    else:
            print('Son todos iguales')
