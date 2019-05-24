# coding:UTF-8
# criador_nota_fiscal.py

from datetime import datetime
from nota_fiscal import NotaFiscal, Item

class CriadorNotaFiscal(object):
    def __init__(self):
        self._cnpj = None
        self._razao_social = None
        self._data_de_emissao = None
        self._detalhes = ''
        self._itens = None

    def com_cnpj(self, cnpj):
        self._cnpj = cnpj
        return self

    def com_razao_social(self, razao_social):
        self._razao_social = razao_social
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self._data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self._itens = itens
        return self

    def constroi(self):
        if self._razao_social is None:
            raise ValueError('Razão social vazia')
        if self._cnpj is None:
            raise ValueError('CNPJ não preenchido')
        if self._itens is None:
            raise ValueError('Itens não preenchidos')
        if self._data_de_emissao is None:
            self._data_de_emissao = datetime.utcnow()

        return NotaFiscal(
            self._razao_social,
            self._cnpj,
            self._itens,
            self._data_de_emissao,
            self._detalhes,
        )

if __name__ == '__main__':
    itens = [
        Item('Descricao item', 50),
        Item('Outro item', 25)
    ]

    nota_fiscal = (
        CriadorNotaFiscal()
        .com_razao_social('Empresa Ficticia')
        .com_cnpj('123123000112')
        .com_itens(itens)
        .constroi()
    )

    print nota_fiscal.razao_social
    print nota_fiscal.cnpj
    print nota_fiscal.data_de_emissao
