# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:29:03 2021

@author: gino_
Trabajo Practico N°1
Ejercicio 13

13.	Se necesita un programa que calcule el índice de masa corporal:
•	El usuario deberá ingresar el peso y la altura de un paciente y el programa deberá informar el valor de IMC y un diagnóstico.
•	El IMC se calcula del siguiente modo: IMC = Peso / (Altura * Altura)
•	El diagnóstico depende del IMC:
o	Si es menos a 20 el peso es “Muy Bajo”
o	De lo contrario, si fuese menor a 30 el peso es “Normal”
o	De lo contrario, si fuese menor a 40 el peso es “Ligero Sobrepeso”
o	De lo contrario, si fuese menor a 50 el peso es “Sobrepeso”

"""

print('Vamos a calcular tu Indice De Masa Corporal o IMC')
Altura = float(input('Ingrese su Altura en Metros: '))
Peso = float(input('Ingrese su Peso en Kg: '))

IMC = Peso / (Altura * Altura)
print(IMC)

if IMC <= 15:
    print('Usted se encuentra en desnutricion, Por favor acuda a un medico')
elif  15<=IMC<=16 :
    print('Tiene un severo caso de delgadez, trate de comer mejor')
elif 16<=IMC<=18.5:
    print('Esta por debajo de su peso normal, trate de comer mas y hacer ejercicio')
elif 18.6<=IMC<=24.9:
    print('Se encuentra en su Peso normal, trate de mantenerse asi')
elif 25<=IMC<=29.9:
    print('Usted tiene un leve sobrepeso')
elif 30<=IMC<=34.9:
    print('Acuda urgentemente a una nutricionista, tiene mucho sobre peso')
elif 35<=IMC<=39.9:
    print('Obesidad Severa')
elif 40<=IMC:
    print('Obesidad Morbida')


