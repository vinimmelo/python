class DescontoPorCincoItens:

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.total_items > 5:
            return orcamento.valor
        return self.__proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        return self.__proximo_desconto.calcula(orcamento)


class SemDesconto:
    def calcula(self, orcamento):
        return 0
