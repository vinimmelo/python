# Should receive a tuple that will update the database.

from collections import OrderedDict

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


def _numeros_desativados(lista_socios) -> dict:
    numero_dos_socios_carteira = [socio['numero'] for socio in carteiras]
    numero_socios = [socio[0] for socio in lista_socios]

    desativados = {}
    for numero in numero_dos_socios_carteira:
        if numero not in numero_socios:
            desativados[numero] = 0

    return desativados


def atualiza_socios(lista_socios):
    desativados = _numeros_desativados(lista_socios)

    ativados = {numero: bilhete for (numero, bilhete) in lista_socios}

    numeros_totais = OrderedDict(sorted({**ativados, **desativados}.items()))

    nova_carteira = []
    for numero, bilhete in numeros_totais.items():
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
