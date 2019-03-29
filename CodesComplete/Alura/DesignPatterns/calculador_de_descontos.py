from descontos import DescontoPorCincoItens
from descontos import DescontoPorMaisDeQuinhentosReais, SemDesconto


class CalculadorDeDescontos:
    def calcula(self, orcamento):
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDeQuinhentosReais(SemDesconto()))

        return desconto.calcula(orcamento)


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = CalculadorDeDescontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print("Desconto calculado de: {:3.2f}".format(desconto))
