import requests
from typing import List
from itmo_test.pokemon_models import *

POKEMONS = []


def get_content() -> List:
    pokemon_content = []
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=50').json()
        pokemon_content = response['results']

    except requests.exceptions.RequestException as err:
        print(err)

    return pokemon_content


def main():
    for i in get_content():
        data = requests.get(i['url']).json()
        POKEMONS.append(Pokemon(id=data['id'],
                                name=i['name'],
                                height=data['height'],
                                weight=data['weight']))


main()

