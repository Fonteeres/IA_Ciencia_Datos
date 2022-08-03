0'
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:23:08 2021
1
@author: gino_
Trabajo Practico N°1
Ejercicio N°11
Se necesita un programa que tenga la siguiente funcionalidad: el 
usuario debe ingresar las tres medidas de los ángulos de un triángulo, 
el programa deberá:
    1.	Verificar que corresponden a un triángulo. Para eso la suma de los tres ángulos debe ser igual a 180 grados.
    2.	Informar que tipo de triángulo es:
    3.	Obtusángulos: uno de los ángulos es mayor a 90 grados.
    4.	Rectángulo: uno de los ángulos es igual a 90 grados.
    5.	Acutángulo: los tres ángulos son menores a 90 grados.
"""

print('Ingresa tres angulos de un triangulo')
print('La suma de las medidas de los tres ángulos internos de un triángulo siempre es 180°')
print('Tambien si un angulo de los 3 es mayor a 90 grados serie un triangulo obtusangulo')
print('Un triangulo es rectangulo si uno de sus angulos es de 90°')
Angulo1 = int(input('Ingresa el primer Angulo: '))
Angulo2 = int(input('Ingresa el segundo Angulo: '))
Angulo3 = int(input('Ingresa el tercer Angulo: '))
print('')

Triangulo = Angulo1 + Angulo2 + Angulo3

if Triangulo == 180:    
    print('es un triangulo')
elif Angulo1<90 and Angulo2<90 and Angulo3<90:
        print('Este triangulo es un acutangulo')
elif Angulo1>90 or Angulo2>90 or Angulo3>90:
        print('Este triangulo es un obtusangulo')
elif Angulo1==90 or Angulo2==90 or Angulo3==90:
        print('Este triangulo es un Rectangulo10')
else:
   print('Los angulos dados no son de un triangulo')
