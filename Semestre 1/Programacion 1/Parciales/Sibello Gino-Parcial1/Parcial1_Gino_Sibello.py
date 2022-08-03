# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:07:06 2021

@author: Gino Sibello
Parcial 1
Tema B
"""

###############################Funciones#####################################
def ContarCaracter():
    Frase = str(input('Ingresar Frase: '))
    Caracter = str(input('Ingresar Caracter: '))
    print('')
    x = 0
    for i in Frase:
        if Caracter == i:
            x = x + 1
    print('El Caracter',Caracter.upper(),'aparece', x, 'veces')
    print('')

def CalcularSumatoria():
    print('Ingresar un numero entero entre 0 y 10')
    print('')
    Numero = int(input('Numero: '))
    print('')
    x = 0
    j = 0
    if   -1 < Numero > 10:
        print('el numero ingresado esta fuera del rango')
    else:
        for i in range(Numero):
            j = j + 1
            x = x + (1 * j)
        print (x)
            

    
def ConsultarPrecio():
    Edad = int(input('Por favor ingrese su edad aqui: '))
    print('')
    if Edad < 4:
        print('La entrada por alguien menor a 4 años es de 25 pesos')
        print('')
    elif 4 <= Edad <= 18:
        print('La entrada por alguien entre 4 y 18 es de 75 pesos')
        print('')
    elif Edad > 18:
        print('La entrada por alguien mayor de edad es de 100 pesos')
        print('')
    

def CalificarAlumno():
    Calificacion = int(input('Ingrese la nota de su calificacion: '))
    print('')
    if Calificacion <= 3:
        print('Calificacion No satisfactoria')
        print('')
    elif Calificacion == 4 :
        print('Calificacion Suficiente')
        print('')
    elif 5 <= Calificacion <= 6:
        print('Calificacion Satisfactoria')
        print('')
    elif Calificacion == 7:
        print('Calificacion Buena')
        print('')
    elif 8 <= Calificacion <= 9: 
        print('Calificacion Muy Buena')
        print('')
    elif Calificacion == 10:
        print('Calificacion Exelente')
        print('')
    else:
        print('El numero Ingresado no corresponde al rango de notas aceptables')
        print('')
        
###################### Ejecuccion del Programa ###############################

print('En este programa Puedes hacer las siguientes Opreraciones:')
print('1 - Conocer cuantos caracteres de un tipo tiene un texto.')
print('2 - Conocer la sumatoria de 0 hasta un numero ingresado por el usario.')
print('3 - Conocer el precio de una entrada. ')
print('4 - Conocer cual es la calificacion cualitativa de un alumno.')
print('5 - Salir del programa')
print('')
Eleccion = int(input('Ingresa el numero que corresponda a tu eleccion: '))
print('')
while Eleccion != 5:
    if Eleccion == 1:
        ContarCaracter()
    elif Eleccion == 2:
        CalcularSumatoria()
    elif Eleccion == 3:
        ConsultarPrecio()
    elif Eleccion == 4:
        CalificarAlumno()
    else:
        print('Esa opccion no esta Disponible')
    print('')
    print('En este programa Puedes hacer las siguientes Opreraciones:')
    print('1 - Conocer cuantos caracteres de un tipo tiene un texto.')
    print('2 - Conocer la sumatoria de 0 hasta un numero ingresado por el usario.')
    print('3 - Conocer el precio de una entrada. ')
    print('4 - Conocer cual es la calificacion cualitativa de un alumno.')
    print('5 - salir del programa')
    Eleccion = int(input('Ingresa el numero que corresponda a tu eleccion: '))

