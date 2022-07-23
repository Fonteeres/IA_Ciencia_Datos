#Haciendo uso de técnicas de scraping se necesita sacar y mostrar todas las materias del tercer y cuarto cuatrimestre de la carrera.
# Ejercicio 2

import requests
from bs4 import BeautifulSoup

response = requests.get(http://127.0.0.1:5500/ia.html)
soup = BeautifulSoup(response.content, 'html.parser')

elemento = soup.find_all('tr','td')
for item in elemento:
    if 
