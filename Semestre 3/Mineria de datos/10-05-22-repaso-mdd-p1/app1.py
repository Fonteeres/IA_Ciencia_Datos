import requests
from bs4 import BeautifulSoup

URL = 'http://127.0.0.1:5500/index.html'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

tags = soup.find_all('li', {'class':'frutas'})
for item in tags:
    print(item.text)

tags_h1 = soup.find_all('h1')
for item in tags_h1:
    print(item.text)

print(soup.title.text)