# uma_string: str = 'Um valor'
# um_inteiro: int = 123456
# um_float: float = 1.23
# um_boloean: bool = True
# um_set: set = {1, 2, 3}
# uma_lista: list = []
# uma_tupla: tuple = 1, 2, 3
# um_dicionario: dict = {}

# uma_string = "223"

# print(uma_string)


# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z


# print(soma(1, 1, 2))


# lista_inteiro: list[int] = [1, 2, 3, 4, 5]
# lista_strings: list[str] = ["a", "b", "c", "d"]
# lista_tuplas: list[tuple] = [(1, "a"), (2, "b")]
# lista_lista_int: list[list[int]] = [[1], [4, 5, 6]]


# um_dict: dict[str, int] = {
#     "A": 0,
#     "B": 0,
#     "C": 0,
# }

# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
# }

# um_set_de_inteiros: set[int] = {1, 2, 3}

ListaInteiros = list[int]  # type alias

DictListaInteiros = dict[str, ListaInteiros]

um_dict_de_listas: dict[str, ListaInteiros] = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}

string_and_integers: str | int = 1  # Union
string_and_integers = "A"  # No erros
string_and_integers = 2  # No erros
lista: list[int | str] = [1, 2, 3, 'a']  # List of integers


# def soma(x: int, y: float | None = 0) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x + x


# print(soma(1, 10))

# from collections.abc import Callable

# SomaInteiros = Callable[[int, int], int]


# def executa(func: SomaInteiros, a: int, b: int) -> int:
#     return func(a, b)


# def soma(a: int, b: int) -> int:
#     return a + b




# print(executa(soma, 1, 2))


# from typing import TypeVar

# T = TypeVar('T')


# def get_item(list: list[T], index: int) -> T:
#     return list[index]


# list_int = get_item([1, 2, 3], 1)  # int
# list_str = get_item(["a", "b", "c"], 1)  # str

from typing import Any

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> list[Person]:
    return [person, person]

# def say_my_name(person: Any):
#     return person.full_name

print(say_my_name(Person("John", "Doe")))