

def soma_dos_multiplos(valor):
    soma = 0
    for i in range(valor):
        if (i % 5 == 0) or (i % 3 == 0):
            soma = i + soma

    return soma

def test_soma_ate_10():
    resultado = soma_dos_multiplos(10)
    assert resultado == 23
