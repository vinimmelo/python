from codes_complete.Alura.leilao.dominio import Leilao, Lance, Avaliador


leilao_celular = Leilao('Leilão de um celular')

lance_john = Lance('john', 100)
lance_gui = Lance('gui', 150)

leilao_celular.lances.append(lance_john)
leilao_celular.lances.append(lance_gui)

avaliador = Avaliador()
avaliador.avalia(leilao_celular)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')


