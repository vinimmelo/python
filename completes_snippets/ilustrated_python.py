def open_file(name, lista):
    with open(name,'w') as fin:
        fin.write('name,adress,age\n')
        for x in lista:
            i = 1
            for j in x:
                if i == len(x):
                    fin.writelines(str(j))
                else:
                    fin.writelines(str(j) + ',')
                i += 1
            fin.writelines('\n')
        return fin

tup1 = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21), ('Vinicius', '45 Batatais', 24)]
nome = r'C:/Users/Vinicius & Thais/Desktop/nome.csv'

def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio

lista_teste = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]


class Cats:
    patas = 4
    olhos = 2
    nariz = 1
    especie = 'Gato'

    def __init__(self, cor: str, idade: int) -> None:
        self.cor = cor
        self.idade = idade

    def __str__(self):
        return "Patas: " + str(self.patas) + " Olhos: " + str(self.olhos) \
            + "\nNariz: " + str(self.nariz) + " Espécie: " + str(self.especie) +\
            "\nCor: " + str(self.cor) + " Idade: " + str(self.idade) + "\n"

class Tiger(Cats):
    especie = 'Tigre'


cat1 = Cats('laranja', 12)
cat2 = Cats('Preto', 10)
tiger1 = Tiger('amarelo', 11)
tiger2 = Tiger('laranja', 12)

if __name__ == '__main__':
    print(tiger2)