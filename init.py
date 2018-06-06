import requests, sqlite3
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html, 'html.parser')

tab = soup.find(id="pokedex")
