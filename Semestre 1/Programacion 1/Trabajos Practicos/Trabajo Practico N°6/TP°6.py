# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 19:18:09 2021

@author: Gino Sibello 
Trabajo Practico N°6
"""

def Consigna1():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    A = int(input('Ingrese la antiguedad: '))
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        datos = a.split(';')
        if int(datos[5]) > A:
            print(datos[1].ljust(20," ") + datos[2].ljust(25," ") + datos[6])
        

def consiga2(): 
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    
    ArchivoSalida = open('DatosProgramaConsigna2.csv', 'tw')
    ArchivoSalida.write('Nombre;Categoria;Sueldo bas;adicional;Presentismo;Total \n')
    
    for i in DatosArchivados:
        i=i.replace('\n', '')
        dato = i.split(';')
        
        Antiguedad = float(dato[6])*(float(dato[5])*(1.2/100))
        Presentismo = (float(dato[6]) + Antiguedad) * (8.35/100)
        total = float(dato[6]) + Antiguedad + Presentismo
        ArchivoSalida.write(dato[1])
        ArchivoSalida.write(';')
        ArchivoSalida.write(dato[2])
        ArchivoSalida.write(';')
        ArchivoSalida.write(dato[6])
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(Antiguedad))
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(Presentismo))
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(total))
        ArchivoSalida.write('\n')
        
    ArchivoSalida.close()
    
def consigna3():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    print('Catgorias: Maestranza; Administrativo; Cajero; Vendedor; Personal Auxiliar; Auxiliar Especializado')
    print('las mayusculas deben ser ingresadas como se muestra arriba')
    A = str(input('Ingrese La categoria que desea: '))
    
    ArchivoSalida = open('DatosProgramaConsigna3.csv', 'tw')
    ArchivoSalida.write('Nombre;Categoria;Sueldo Bas. \n')
    for i in DatosArchivados:
        i = i.replace('\n', '')
        datos = i.split(';')
        if A ==str(datos[2]):
            ArchivoSalida.write(datos[1])
            ArchivoSalida.write(';')
            ArchivoSalida.write(datos[2])
            ArchivoSalida.write(';')
            ArchivoSalida.write(datos[6])
            ArchivoSalida.write('\n')
    print('Datos Exportados')
    ArchivoSalida.close()
    
def consigna4():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    a = str(input('Ingrese antiguedad: '))
    
    ArchivoSalida = open('DatosProgramaConsigna4.csv', 'tw')
    ArchivoSalida.write('Nombre;Categoria;Sueldo bas \n')
    
    for i in DatosArchivados:
        i=i.replace('\n', '')
        dato = i.split(';')
        if a > str(dato[5]):
            
            ArchivoSalida.write(dato[1])
            ArchivoSalida.write(';')
            ArchivoSalida.write(dato[2])
            ArchivoSalida.write(';')
            ArchivoSalida.write(dato[6])
            ArchivoSalida.write('\n')
    ArchivoSalida.close()

def consigna5():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    A = str(input('Ingrese legajo: '))
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        datos = a.split(';')
        if A == str(datos[0]):
            Antiguedad = float(datos[6])*(float(datos[5])*(1.2/100))
            Presentismo = (float(datos[6]) + Antiguedad) * (8.35/100)
            total = float(datos[6]) + Antiguedad + Presentismo
            print('Nombre: '  + datos[1] + ' ;Categoria: ' + datos[2])
            print('Sueldo bas: ' + str(datos[6]) + ' ;Adicional ' + str(Antiguedad))
            print('Presentismo: ' + str(Presentismo) + ' ;Total: ' + str(total))
            
def consigna6():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Contador = Contador + float(dato[6])    
    print('Total de sueldos: ' + str(Contador))
def consigna7():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    Suma = 0
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Contador = Contador + float(dato[6])
        Suma = Suma + 1
    print('Promedio de sueldos: ' + str(Contador/Suma))
def consigna8():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Cantidad = 0
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
    
        if str(dato[6]) > str(Cantidad):
            Cantidad = dato[6]
    print('Nombre: ' + dato[1] + ' ;Sueldo Bas: ' + Cantidad)     
    
def consigna9():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Antiguedad = float(dato[6])*(float(dato[5])*(1.2/100))
        Contador = Contador + Antiguedad
    print('Total de Antiguedad: ' + str(Contador))
    
def consigna10():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    Cantidad = 0
    
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Antiguedad = float(dato[6])*(float(dato[5])*(1.2/100))
        Cantidad = Cantidad + 1 
        Contador = Contador + Antiguedad
    promedio = Contador/Cantidad
    print('El Promedio Por antiguedad es de: ' + str(promedio))  

def consgina11():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Antiguedad = float(dato[6])*(float(dato[5])*(1.2/100))
        Presentismo = (float(dato[6]) + Antiguedad) * (8.35/100)
        Contador = Contador + Presentismo 
    print('Total de Antiguedad: ' + str(Contador))
    
def consigna12():
    Archivo = open('DatosPrograma.csv','tr')
    DatosArchivados = Archivo.readlines()
    Archivo.close()
    Contador = 0
    Cantidad = 0
    
    
    for a in DatosArchivados:
        a = a.replace('\n', '')
        dato = a.split(';')
        Antiguedad = float(dato[6])*(float(dato[5])*(1.2/100))
        Presentismo = (float(dato[6]) + Antiguedad) * (8.35/100)
        Cantidad = Cantidad + 1 
        Contador = Contador + Presentismo
    promedio = Contador/Cantidad
    print('El Promedio Por antiguedad es de: ' + str(promedio)) 