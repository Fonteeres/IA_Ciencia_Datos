# MODULOS

import requests
import re
from bs4 import BeautifulSoup

# CUIT BIEN FORMADOS

def parte2():

    EXPRESION = '(^[2-3]0-| [2-3]0-)([0-9]{8}-)(\d |\d$)'
    URL = 'http://127.0.0.1:5500/data.json'

    response = requests.get(URL)
    filas = response.json()

    for fila in filas:
        res = re.findall(EXPRESION, fila['contenido'])
        if res:
            print('{} - {}'.format(fila['linea'], fila['contenido']))

def parte3():
    URL = 'http://127.0.0.1:5500/ia.html'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tags_tr = soup.find_all('tr')
    for tag_tr in tags_tr:
        tags_td = tag_tr.find_all('td')
        if len(tags_td) > 0:
            if tags_td[2].text=='4' or tags_td[2].text=='5':
                print('{} - {}'.format(tags_td[0].text, tags_td[1].text))


parte2()
#parte3()
