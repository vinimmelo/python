from unittest import TestCase

from codes_complete.Alura.leilao.dominio import Leilao, Lance, Avaliador


class TestAvaliador(TestCase) :
    def test_avalia(self) :
        leilao_celular = Leilao('Leilão de um celular')

        lance_john = Lance('john', 100)
        lance_gui = Lance('gui', 150)

        leilao_celular.lances.append(lance_john)
        leilao_celular.lances.append(lance_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao_celular)

        self.assertEqual(avaliador.maior_lance, 150)
        self.assertEqual(avaliador.menor_lance, 100)
