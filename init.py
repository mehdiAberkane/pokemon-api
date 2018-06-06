import requests, sqlite3
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html, "html.parser")

tab = soup.find(id="pokedex")
for link in tab.find_all("tr"):
    for l in link.find_all("td"):
        print(l.text)
        print("\n")
