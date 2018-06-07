import requests, mysql.connector
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/all"

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1')

cursor = cnx.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS pokemon')
cursor.connect('pokemon')
cursor.execute('CREATE TABLE IF NOT EXISTS pokemon ('
                'id INT PRIMARY KEY NOT NULL AUTO_INCREMENT',
                'name varchar(100)',
               ')')
cursor.execute('INSERT INTO "pokemon" (name) VALUES ("toto")')

'''
response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html, "html.parser")

tab = soup.find(id="pokedex")
for link in tab.find_all("tr"):
    tab = []
    for l in link.find_all("td"):
        tab.append(l.text)
    if len(tab) > 0:
        print("\n")
        print(tab)
'''