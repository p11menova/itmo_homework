from dataclasses import dataclass
import requests

BASE_POKEMONS = []
POKEMONS = []


class BasePokemon:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f'name: {self.name}'

    def get_base_name(self) -> str:
        return self.name


class PokemonStats:
    def __init__(self, *args):
        self.args = args

    @property
    def stats(self):
        my_iter = iter(self.args)
        return f'hp: {next(my_iter)}; attack: {next(my_iter)}; defense: {next(my_iter)}; ' \
            f'special_attack: {next(my_iter)}; special_defense: {next(my_iter)}; speed: {next(my_iter)}'

@dataclass
class Pokemon(BasePokemon):
    __id: int
    __url: str
    __name: str
    __height: int
    __weight: int

    stats: PokemonStats = None

    def __str__(self) -> str:
        return f'id: {self.__id}, name: {self.get_name()}, ' \
            f'height: {self.__height}, weight: {self.__weight}'

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_weight(self) -> int:
        return self.__weight

    def get_url(self) -> str:
        return self.__url


class PokeError(Exception):
    pass


class PokeAPI:
    def get_pokemon(self, key: int or str) -> str:
        pokemon = None
        if isinstance(key, int):
            pokemon = list(filter(lambda x: x.get_id() == key, POKEMONS))[0]
        elif isinstance(key, str):
            pokemon = list(filter(lambda x: x.get_name() == key, POKEMONS))[0]

        else:
            raise PokeError('такого покемона нет в списке!')

        data = requests.get(pokemon.get_url()).json()['stats']

        pokemon.stats = PokemonStats(data[0]['base_stat'],
                                     data[1]['base_stat'],
                                     data[2]['base_stat'],
                                     data[3]['base_stat'],
                                     data[4]['base_stat'],
                                     data[5]['base_stat'])
        return '\n'.join(["pokemon's DESCRIPTION:",  str(pokemon), "pokemon's STATS:", pokemon.stats.stats, '\n'])

    def get_all(self, get_full: bool):
        if not get_full:
            if not BASE_POKEMONS:
                raise PokeError('список покемонов пуст!')

            cur_num = 0
            pokems_num = len(BASE_POKEMONS)

            while cur_num < pokems_num:
                yield str(BASE_POKEMONS[cur_num])
                cur_num += 1

            return None

        if not POKEMONS:
            raise PokeError('список покемонов пуст!')

        cur_num = 1
        pokems_num = len(POKEMONS)

        while cur_num <= pokems_num:
            yield self.get_pokemon(key=cur_num)
            cur_num += 1
