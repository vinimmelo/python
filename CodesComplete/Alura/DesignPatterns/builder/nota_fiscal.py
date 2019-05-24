# coding:UTF-8
# nota_fiscal.py


class NotaFiscal(object):
    def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes):
        self._razao_social = razao_social
        self._cnpj = cnpj
        self._itens = itens
        self._data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes nota fiscal não pode ter mais do que 30 caracteres')
        self._detalhes = detalhes

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


