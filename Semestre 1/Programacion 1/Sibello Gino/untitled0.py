# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:29:55 2021

@author: Gino Sibello
"""

def MostrarSueldos():
    Archivo = open('IEFI.csv','tr')
    Lector = Archivo.readlines()
    Archivo.close()
    
    for i in Lector:
        i = i.replace('\n', '')
        dato = i.split(';')
        print('')
        print('Nombre , Apellido ; Sueldo Basico ; Aumento 1; Aumento 2')
        Aumento1 = float(dato[5]) *(12/100)
        Aumento2 = Aumento1 * (14/100)
        
        print(dato[1]+ ', '  + dato[2] + ' ; ' + dato[5] + ' ; '+ str(Aumento1)+ ' ; ' + str(Aumento2))

def calcularPromedio():
    Archivo = open('IEFI.csv','tr')
    Lector = Archivo.readlines()
    Archivo.close()
    Contador = 0
    Total = 0
    
    for i in Lector:
        i = i.replace('\n', '')
        dato = i.split(';')
        Contador = Contador + 1
        Total = Total + float(dato[5]) 
        
    print('El Promedio de los sueldos es: ' + str(Total/Contador))

def ExportarSueldos():
    Archivo = open('IEFI.csv','tr')
    Lector = Archivo.readlines()
    Archivo.close()
    Adicional = 0
    
    
    ArchivoSalida = open('DatosExportados.csv', 'tw')
    ArchivoSalida.write('Nombre; Sueldo Basico; Ad x Antiguedad; Total a Cobrar \n')
    for i in Lector:
        i = i.replace('\n', '')
        dato = i.split(';')
        Adicional = float(dato[5]) *(1.5/100)
        Total = float(dato[5]) + Adicional
        ArchivoSalida.write(dato[1] + ', ' + dato[2])
        ArchivoSalida.write(';')
        ArchivoSalida.write(dato[5])
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(Adicional))
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(Total))
        ArchivoSalida.write('\n')
        
    ArchivoSalida.close()
    print('Datos Exportados, si quiere ver mas abra el archivo DatosExportados')
    
def ConsultarUnAumentoDeSueldo():
    Archivo = open('IEFI.csv','tr')
    Lector = Archivo.readlines()
    Archivo.close()
    A = input('Introduzca su Numero De legajo: ')
    
    for i in Lector:
        i = i.replace('\n', '')
        dato = i.split(';')
        if A == str(dato[0]):
            print('Nombre: '+dato[1] + ', ' + dato[2])
            print('Sueldo Basico: ' + dato[5])
            print('Sueldo Con Aumento: ' + str( float(dato[5])+ float(dato[5]) * (12/100)))
            
print('Este Programa puede hacer las siguientes opreaciones: ')
print('1 -listar los sueldos')
print('2 -Exportar los sueldos')
print('3 -Calcular el promedio del sueldo basico')
print('4 -Consultar el aumento de sueldo de un empleado')

A = int(input('Ingresa el Numero que corresponde a tu eleccion: '))
if A == 1:
    MostrarSueldos()
elif A == 2:
    calcularPromedio()
elif A == 3:
    ExportarSueldos()
elif A == 4:
    ConsultarUnAumentoDeSueldo()
else: 
        print('Esa opccion no esta disponible, Ingrese otra de nuevo')
        