# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:40:03 2021

@author: Gino Sibello
"""
########## Ejercicios ##############

# Ejercicio N°1
def ListadoDeMozos():
    ListaDeMozos = open('Mozos.csv', 'tr')
    Resultado = ListaDeMozos.readlines()
    for i in Resultado:
        fila = i.split(";")
        print (" Nombre: " + fila[1] + "\n", "Categoria: " + fila[2] + "\n", "Porcentaje a cobrar: " + fila[3] + "%" )
        print ("")
    ListaDeMozos.close()
    
#Ejercicio N°2

def ListadoDeCategoriasEspecifico():
    print('En este Archivo solo tenemos la categorias "Experto" , "Juniors" y "Master" ')
    Decision = input(str('Ingrese La categoria que desea conocer: '))
    Archivo = open('Mozos.csv', 'tr')
    Lectura = Archivo.readlines()
    for i in Lectura: 
        fila = i.split(';')
        if fila[2] == Decision:
            print(i)
    Archivo.close()
        
#Ejercicios N°3

def listadoMozosPunto3():
    ArchiMozos = open('Mozos.csv', 'tr')
    DatosArchivo = ArchiMozos.readlines()
    ArchiMozos.close()
    importe = float(0)
    
    
    ArchivoSalida = open ('Salida.csv', 'tw')
    ArchivoSalida.write('Nombre;Categoria;Importe\n')
    for x in DatosArchivo:
        x = x.replace("\n","")
        datos = x.split(";")
        importe = float(datos[3]) * float(datos[4])/100
        ArchivoSalida.write(str(datos[1]))
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(datos[2]))
        ArchivoSalida.write(';')
        ArchivoSalida.write(str(datos[3])) 
        ArchivoSalida.write(str(importe).replace('.',','))
        ArchivoSalida.write('\n')
    ArchivoSalida.close()
    print('Datos Exportados')

#Ejercicio 4
def listaMozosPunto4():    
    #Datos que debe ingresar el usuario
    print('En este Archivo solo tenemos la categorias "Experto" , "Juniors" y "Master" ')
    Decision = input(str('Ingrese La categoria que desea conocer: '))
    #Lectura del archivo original
    Archivo = open('Mozos.csv', 'tr')
    Lectura = Archivo.readlines()
    Archivo.close()
    
    #Creacion del nuevo archivo
    ArchivoSalida = open ('ListadoMozosDecision.csv', 'tw')
    ArchivoSalida.write('Legajo;Nombre;Porcentaje De Comision;Ventas\n')
    for i in Lectura:
        i = i.replace("\n", "")
        fila = i.split(";")
        if fila[2] == Decision:
            ArchivoSalida.write(fila[0])
            ArchivoSalida.write(';')
            ArchivoSalida.write(fila[1])
            ArchivoSalida.write(';')
            ArchivoSalida.write(fila[3])
            ArchivoSalida.write(';')
            ArchivoSalida.write(fila[4]+ '\n')
    ArchivoSalida.close()
    print('Datos Exportados')

#Ejercicio 5
def TotalDeVentas():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    Contador = 0
    
    for i in Lectura:
        i = i.replace("\n", "")
        Dato = i.split(";")
        Contador = Contador + int(Dato[4]) 
        
    print('La suma total de todas las ventas es ' + str(Contador) + ' ventas')
    
# Ejercicio 6
def PromedioDeVentas():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    Contador = 0
    total = 0
    
    for i in Lectura:
        i = i.replace("\n", "")
        Dato = i.split(";")
        Contador = Contador + int(Dato[4]) 
        total = total + 1
    Promedio = int(Contador/total)
        
    print('El promedio total de todas las ventas es ' + str(Promedio) + ' ventas')
    
# Ejercicio 7
def MozoConLaMayorVenta():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    Venta1 = 0
    
    for i in Lectura:
        i = i.replace("\n", '')
        Dato = i.split(";")
        if Venta1 < int(Dato[4]):
            Venta1 = int(Dato[4])
            Nombre = Dato[1]
                
                
    print(Venta1)
    print(Nombre)


def TotalDeComisionDeVentas():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    TotalComisiones = 0
    importe = 0
    
    for i in Lectura:
        i = i.replace("\n", '')
        Dato = i.split(";")
        importe = (float(Dato[3]) * float(Dato[4])/100)
        TotalComisiones = TotalComisiones + importe     
    
    print('Calculo Final: ' + str(TotalComisiones))
    
    

def PromedioDelTotalDeVentas():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    TotalComisiones = 0
    importe = 0
    contador = 0
    
    for i in Lectura:
        i = i.replace("\n", '')
        Dato = i.split(";")
        contador = contador + 1
        importe = (float(Dato[3]) * float(Dato[4])/100)
        TotalComisiones = TotalComisiones + importe
    PromedioDeComisiones = TotalComisiones/contador
    
    print('Calculo Final: ' + str(TotalComisiones))
    print('Promedio Final: ' + str(PromedioDeComisiones))
    # aca como el anterior tiene un error lo estoy arrastrando
    

def PromedioMayorImporteAPagar():
    ArchivoMozos = open('Mozos.csv', 'tr')
    Lectura = ArchivoMozos.readlines()
    ArchivoMozos.close()
    TotalComisiones = 0
    importe = 0
    contador = 0
    MayorImporte = 0
    
    for i in Lectura:
        i = i.replace("\n", '')
        Dato = i.split(";")
        contador = contador + 1
        importe = (float(Dato[3]) * float(Dato[4])/100)
        TotalComisiones = TotalComisiones + importe
        if MayorImporte < importe:
            MayorImporte = importe
    
    
    print('El Mayor importe a pagar es de: ' + str(MayorImporte))
    

    
    
    
    
    
    
    
    
