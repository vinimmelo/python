# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod


class EstadoDeUmOrcamento(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * .02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovação não pode ir para finalizado.')


class Aprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * .05)

    def aprova(self, orcamento):
        raise Exception('Orcamento já está em estado de aprovação.')

    def reprova(self, orcamento):
        raise Exception('Orcamento já está em estado de aprovação e não pode ser reprovado.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de reprovação')

    def finaliza(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser finalizado')


class Finalizado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados não recebem desconto.')

    def aprova(self, orcamento):
        raise Exception('Orcamento finalizado já foi aprovado.')

    def reprova(self, orcamento):
        raise Exception('Orcamento já finalizado não pode ser reprovado.')

    def finaliza(self, orcamento):
        raise Exception('Orcamento já foi finalizado.')


class Orcamento(object):
    def __init__(self):
        self.__items = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    @property
    def valor(self):
        total = 0.0
        for item in self.__items:
            total += item.valor
        return total - self.__desconto_extra

    def obter_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def adiciona_item(self, item):
        self.__items.append(item)


class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('item 1', 100))
    orcamento.adiciona_item(Item('item 2', 50))
    orcamento.adiciona_item(Item('item 3', 400))

    print orcamento.valor

    orcamento.aplica_desconto_extra()

    print orcamento.valor

    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print orcamento.valor

    orcamento.finaliza()
    print type(orcamento.estado_atual)
