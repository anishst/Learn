import random

import requests
import pokebase
#https://medium.com/@sergio13prez/fetching-them-all-poke-api-62ca580981a2
# https://pokeapi.co/docs/v2#resource-listspagination-section
#https://pokeres.bastionbot.org/images/pokemon/${pokeID}.png
#https://pokeapi.co/api/v2/pokemon/1/
# https://github.com/PokeAPI/pokebase

# Arrange
url = 'https://pokeapi.co/api/v2/pokemon'

rand_num = random.randrange(1,1000)
url2 = f'https://pokeapi.co/api/v2/pokemon/1/'
# Act
response = requests.get(url2)
results = response.json()
print(results["id"])
print(results["name"])
types = (results["types"])
for item in types:
    print(item["type"]["name"])
print(type(results))



