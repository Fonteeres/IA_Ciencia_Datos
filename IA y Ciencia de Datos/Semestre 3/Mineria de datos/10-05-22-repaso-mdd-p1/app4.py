
import requests

URL = 'https://jsonplaceholder.typicode.com/comments'
response = requests.get(URL)
filas = response.json()
for fila in filas:
    print('id: {}'.format(fila['email']))
