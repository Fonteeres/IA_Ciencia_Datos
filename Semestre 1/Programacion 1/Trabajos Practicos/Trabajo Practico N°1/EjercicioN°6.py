# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:27:35 2021

@author: gino_
Trabajo Practico N°1
Ejercicio N°6
Se necesita un programa que tenga la siguiente funcionalidad: el usuario 
debe ingresar el importe de una compra que quiere realizar e informar si 
la misma es de contado, tarjeta de crédito, cheque o cuenta corriente. 
El programa deberá mostrar el importe a pagar, teniendo en cuenta 
las siguientes reglas:
    •	Contado: el importe a pagar es igual al importe de venta.
    •	Tarjeta de Crédito: el importe a pagar es igual al importe de venta con un aumento del 2 %.
    •	Cheque: el importe a pagar es igual al importe de venta con un aumento del 3 %.
    •	Cuenta Corriente: el importe a pagar es igual al importe de venta con un aumento del 1,5 %.
"""
print('Bienvenido al SuperMercado VEO!')
Precio = float(input('Por favor ingrese el monto a pagar: '))
print('')
print('Ingrese el metodo con el que quiere pagar')
print('')
print('Contado = cont, tarjeta de credito = credito,')
print('cheque = cheque o Cuenta Corriente = cc ')
ModoDePago = str(input('Metodo a pagar: '))

if ModoDePago == 'credito':
    Porcentaje = Precio * 0.2
    print('El monto a pagar con tarjeta de credito es de: ',Precio + Porcentaje)
elif ModoDePago == 'cheque':
    Porcentaje = Precio * 0.3
    print('El monto a pagar con cheque es de: ', Precio + Porcentaje)
elif ModoDePago == 'cc':
    Porcentaje = Precio * 0.15
    print('El monto a pagar con cuenta corriente es de: ', Precio + Porcentaje)
elif ModoDePago == 'cont':
    print('De contado no tiene recargo, ustede debe pagar: ', Precio)
else: 
    print('El metodo de pago ingresado no es correcto por favor revise')
    print('si lo escribio correctamente y sin mayusculas')
    
    
