import requests

def getApi(URL):
    response = requests.get(URL)
    filas = response.json()
    return filas


def createCsv(filas):
    with open('datos.csv', 'w') as archivo:
        archivo.write('name, city')
        archivo.write('\n')
        for fila in filas:
            archivo.write(fila['name'])
            archivo.write(', ')
            archivo.write(fila['address']['city'])
            archivo.write('\n')


#filas = getApi('https://api.mercadolibre.com/classified_locations/countries')
# for fila in filas:
#    print('id: {} - nombre: {}'.format(fila['id'], fila['name']))

filas = getApi('https://jsonplaceholder.typicode.com/users')
#for fila in filas:
#    print('name: {} city: {} '.format(fila['name'], fila['address']['city']))

createCsv(filas)
