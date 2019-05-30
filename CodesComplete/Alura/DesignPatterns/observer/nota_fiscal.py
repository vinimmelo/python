# coding:UTF-8
# nota_fiscal.py
from datetime import date
from observadores import __all__

class NotaFiscal(object):
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
        self._razao_social = razao_social
        self._cnpj = cnpj
        self._itens = itens
        self._data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes nota fiscal não pode ter mais do que 30 caracteres')
        self._detalhes = detalhes

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self._razao_social

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def itens(self):
        return self._itens

    @property
    def data_de_emissao(self):
        return self._data_de_emissao


class Item(object):
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


if __name__ == '__main__':
    itens=[Item('Item 1', 100), Item('Item 2', 200)]

    nota_fiscal = NotaFiscal(
            cnpj='0123456789120',
            razao_social='FHSA limitada',
            itens=itens,
            observadores=__all__,
    )
