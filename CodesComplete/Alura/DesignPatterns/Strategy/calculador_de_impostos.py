from Strategy.impostos import calcula_icms, calcula_iss

class Calculador_de_impostos:

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    from Strategy.orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, calcula_icms)
    calculador_de_impostos.realiza_calculo(orcamento, calcula_iss)
