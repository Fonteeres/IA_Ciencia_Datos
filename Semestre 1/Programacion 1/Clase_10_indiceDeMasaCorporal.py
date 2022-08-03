# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:58:10 2021

@author: gino_




indice de masa corporal como medirlo
determinar si una persona esta normal
con sobre peso o por debajo de su peso ideal
IMC = peso / (altura * altura)
"""
print ('Indice de Masa Corporal')
print (' Dime tu altura y tu peso y asi puedo calcularlo por usted')
print ('')

peso = float (input('Indicar Peso: '))
altura = float (input ('Indicar Altura: '))

imc = peso / (altura ** 2)

diagnostico = ''
if imc < 18.5:
    diagnostico = 'Ustedes Posee un IMC muy bajo, ¡deberia comermas!'
elif imc < 24.9:
        diagnostico = 'Usted posee un IMC normal, ¡Continue asi!'
elif imc < 29.9:
        diagnostico = 'Usted posee un IMC que indica sobre peso, ¡gordo culiao!'
else: 
        diagnostico = 'Mucho Sobre peso'
        

print('Su indice de Masa Corporal es', imc)
print ('Diagnostico', diagnostico)


