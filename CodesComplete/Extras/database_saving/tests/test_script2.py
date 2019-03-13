from CodesComplete.Extras.database_saving.script import atualiza_socios


def test_atualiza_socios():
    lista_socios = [
        (1, 16),
        (3, 13),
        (5, 15),
        (8, 10),
        (9, 19),
    ]
    expected = [
        {
            'numero': 1,
            'ativo': True,
            'bilhete': 16,
        },
        {
            'numero': 2,
            'ativo': False,
            'bilhete': 0,
        },
        {
            'numero': 3,
            'ativo': True,
            'bilhete': 13,
        },
        {
            'numero': 4,
            'ativo': False,
            'bilhete': 0,
        },
        {
            'numero': 5,
            'ativo': True,
            'bilhete': 15,
        },
        {
            'numero': 6,
            'ativo': False,
            'bilhete': 0,
        },
        {
            'numero': 8,
            'ativo': True,
            'bilhete': 10,
        },
        {
            'numero': 9,
            'ativo': True,
            'bilhete': 19,
        },
    ]

    result = atualiza_socios(lista_socios)
    assert result == expected
