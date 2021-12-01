import requests
from typing import List
from itmo_test.pokemon_models import *


def get_content(limit=700) -> List:
    pokemon_content = []
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/', params={'limit': limit}).json()
        pokemon_content = response['results']

    except requests.exceptions.RequestException as err:
        print(err)

    return pokemon_content


def make_pokemons(content: List) -> None:
    for i in content:
        BASE_POKEMONS.append(BasePokemon(i['name']))
        data = requests.get(i['url']).json()

        POKEMONS.append(Pokemon(data['id'],
                                i['url'],
                                i['name'],
                                data['height'],
                                data['weight']))


def main():
    make_pokemons(get_content(5))
    pa = PokeAPI()

    for p in pa.get_all(get_full=False):
        print(p)

    #task 1
    # make_pokemons(get_content())
    # pok_api = PokeAPI()
    # print(pok_api.get_pokemon(key='ditto'))
    #
    # #task 2
    # make_pokemons(get_content(50))
    # pok_api2 = PokeAPI()
    # poks = sorted(pok_api2.get_all(get_full=True), key=lambda x: x.get_weight(), reverse=True)
    # print(poks[0])


main()


