# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:56:09 2021

@author: Gino Sibello
"""
import os
import pyodbc


def listar():
    NombreDriver = 'Microsoft Access Driver (*.mdb, *.accdb)'
    # En esta variable dejo en claro cual es el tipo de base de datos que voy a usar y sus extenciones
    # Asi como se muestra en coneccion luego llamo la variable asi con la libreria que importe
    # Pyodbc me conecto a la base de datos y uso el NombreDriver para decirle cual es esa base de datos
    # .mdb Son archivos de las versiones viejas y .accdb Son archivos de las nuevas versiones
    NombreBaseDeDatos = os.getcwd() + '\Libreria_2_1.mdb'
    # En esta variable guardo donde se encuentra mi archivo en el disco 
    # Mediante el uso de la otra libreria que importe 'os' Puedo determinar en que parte de mi disco esta
    # el Archivo que busco sin necesidad de escribir toda la ruta, ademas de que esta sujeto a errores si
    # escribo toda la ruta porque si lo comparto con alguien mas puede que su ruta sea diferente
    
    Coneccion = pyodbc.connect(f"Driver = {NombreDriver}; DBQ = {NombreBaseDeDatos}")
    # Mediante esta variable me conecto a la base de datos, con la informacion de las variables anteriores
    # osea con la ubicacion de el archivo que quiero usar y con el tipo de base de datos que voy a usar y su extencion
    Cursor = Coneccion.cursor()
    # El cursor es el elemento que realmente va a estar trabajando sobre la base de datos 
    
    Cursor.execute('select * from idioma')
    
    for registro in Cursor.fetchall():
        print(str(registro[0].rjust(2) + '   ' + registro[1])) 
        #se imprimen las filas de la base de datos
    Cursor.close()
    Coneccion.close()
    
    
listar()