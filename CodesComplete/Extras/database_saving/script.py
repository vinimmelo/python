# Should receive a tuple that will update the database.

from collections import OrderedDict, Counter

carteiras = [
    {
        'numero': 1,
        'ativo': True,
        'bilhete': 10,
    },
    {
        'numero': 2,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 3,
        'ativo': True,
        'bilhete': 12,
    },
    {
        'numero': 4,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 5,
        'ativo': True,
        'bilhete': 14,
    },
    {
        'numero': 6,
        'ativo': True,
        'bilhete': 15,
    },
]


def _lista_atualizada(lista_socios):
    ativados = {numero: bilhete for (numero, bilhete) in lista_socios}
    todos_os_socios = OrderedDict(((socio['numero'], 0) for socio in carteiras))
    todos_os_socios.update(ativados)
    return todos_os_socios


def atualiza_socios(lista_socios):
    todos_os_socios = _lista_atualizada(lista_socios)

    nova_carteira = []
    for numero, bilhete in todos_os_socios.items():
        if bilhete == 0:
            resultado = _atualiza_carteira(numero, False, bilhete)
        else:
            resultado = _atualiza_carteira(numero, True, bilhete)
        nova_carteira.append(resultado)

    return nova_carteira


def _atualiza_carteira(numero, ativo, bilhete) -> dict:
    result = {
        'numero': numero,
        'ativo': ativo,
        'bilhete': bilhete
    }
    return result
