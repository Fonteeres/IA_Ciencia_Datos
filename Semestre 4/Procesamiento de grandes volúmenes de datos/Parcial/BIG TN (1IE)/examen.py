
# IMPORTAR MODULOS


# PARTE 1

'''
	Completar en las siguientes fuentes de datos a que tipos corresponden,
	ESTRUCTURADO, SEMI-ESTRUCTURADO O NO ESTRUCTURADO.

	Un archivo en formato XML: ESTRUCTURADO
	Un archivo en formato JSON: SEMI-ESTRUCTURADO
	Un documento de WORD: ESTRUCTURADO
	Un archivo de texto: NO ESTRUCTURADO
	Un archivo CSV: SEMI-ESTRUCTURADO
	Una tabla de una base de datos MySQL: ESTRUCTURADO
	Una colección de un base de datos MongoDB: SEMI-ESTRUCTURADO

'''

# PARTE 2

'''
	docker run -it --name alumno-ubuntu ubuntu:18.04
	exit
	Docker ps -a
	docker start alumno-ubuntu
	docker exec -it alumno-ubuntu bash
	--Dentro de linux:
		adduser ies
		login ies
		mkdir datos
		mkdir copia
		cd datos
		cat > hola.txt
		hola a todos
		cat > chau.txt
		chau a todos
		ls
		cp chau.txt /home/ies/copia
		cp hola.txt /home/ies/copia
		chmod 740 chau.txt
		chmod 740 hola.txt
		logout
		exit
	docker stop alumno-ubuntu
	docker rm alumno-ubuntu
	docker ps -a
	docker images (para ver el nombre)
	dokcer rmi 35b3f

'''

# PARTE 3

'''
	!pip install pymongo
	from pymongo import MongoClient
	import pandas as pd
	df = pd.read_json('data.json') #LLamo el archivo
	cantidad = df.groupby('car_make')['id'].count().reset_index(name='Cantidad') #Cuento la cantidad de personas por auto
	MONGO_URI = 'mongodb://localhost:27099'
	cliente = MongoClient(MONGO_URI)
	db = cliente['midb']
	coleccion = db['micoleccion']
	for index, row in cantidad.iterrows():
    	coleccion.insert_one({'Marca_Auto':row["car_make"], 'Cantidad': row["Cantidad"]})
'''
