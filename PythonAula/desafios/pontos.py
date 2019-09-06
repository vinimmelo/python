# pontos.py

def adiciona_pontos(palavra):
    if not palavra:
        return ''

    return '.'.join(list(palavra))


def remove_pontos(palavra):
    if not palavra:
        return ''

    return palavra.replace('.', '')


def test_adiciona_pontos():
    resultado = adiciona_pontos('teste')
    assert resultado == 't.e.s.t.e'

def test_adiciona_pontos_incorreto():
    resultado = adiciona_pontos('')
    assert resultado == ''

def test_adiciona_pontos_none():
    resultado = adiciona_pontos(None)
    assert resultado == ''

def test_adiciona_pontos_dois():
    resultado = adiciona_pontos('resultado')
    assert resultado == 'r.e.s.u.l.t.a.d.o'




def test_remove_pontos():
    resultado = remove_pontos('t.e.s.t.e')
    assert resultado == 'teste'

def test_remove_pontos_dois():
    resultado = remove_pontos('r.e.s.u.l.t.a.d.o')
    assert resultado == 'resultado'

def test_remove_pontos_incorreto():
    resultado = remove_pontos('')
    assert resultado == ''

def test_remove_pontos_none():
    resultado = remove_pontos(None)
    assert resultado == ''
