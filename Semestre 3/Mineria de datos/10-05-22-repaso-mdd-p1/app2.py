import requests
import pandas as pd

from bs4 import BeautifulSoup

URL = 'https://www.musimundo.com/telefonia/telefonos-celulares/c/82?q=%3Arelevance&page=0'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

lista = []
tags = soup.find_all('p', {'class':'mus-pro-name'})
for item in tags:
    lista.append(item.text.strip())

df = pd.DataFrame(lista)
df.to_csv("miguel.csv")




