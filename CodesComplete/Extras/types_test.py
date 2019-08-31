from typing import NamedTuple


class Teste(NamedTuple):
    """NamedTuple test"""
    aa: str
    bb: str


if __name__ == '__main__':
    teste = Teste('Eita', 'Uowww')
    print(teste)
