BASE_POKEMONS = []
POKEMONS = []


class BasePokemon:
    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f'name: {self.__name}'

    def get_name(self) -> str:
        return self.__name


class Pokemon(BasePokemon):
    def __init__(self, id:int, name:str, height:int, weight:int) -> None:
        BasePokemon.__init__(self, name)

        self.__id = id
        self.__name = name
        self.__height = height
        self.__weight = weight

    def __str__(self) -> str:
        return f'id: {self.__id}, name: {self.__name}, ' \
            f'height: {self.__height}, weight: {self.__weight}'

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_weight(self) -> int:
        return self.__weight


class PokeError(Exception):
    pass


class PokeAPI:
    def get_pokemon(self, key: int or str) -> str:
        if isinstance(key, int):
            return list(filter(lambda x: x.get_id() == key, POKEMONS))[0]
        elif isinstance(key, str):
            return list(filter(lambda x: x.get_name() == key, POKEMONS))[0]

        raise PokeError('такого покемона нет в списке!')

    def get_all(self, get_full: bool):
        if not get_full:
            if not BASE_POKEMONS:
                raise PokeError('список покемонов пуст!')
            return '\n'.join([str(j) for j in BASE_POKEMONS])

        if not POKEMONS:
            raise PokeError('список покемонов пуст!')

        cur_num = 1
        pokems_num = len(POKEMONS)

        while cur_num <= pokems_num:
            yield self.get_pokemon(key=cur_num)
            cur_num += 1
