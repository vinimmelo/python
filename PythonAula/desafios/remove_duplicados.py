"""Remove duplicados dos arquivos"""
# Escreva uma função que encontre os números duplicados
# e devolva-os em uma lista.

# Dicas:
#     Faça testes unitários
#     Use a função open()
#     Lembre-se do tipo especial set


def transforma_em_lista(arquivo):
    """Transforma arquivo em lista"""
    lista = arquivo.split("\n")
    return lista


def abre_arquivo(caminho):
    """Abre arquivos"""
    with open(caminho, 'r') as arquivo:
        return arquivo.read()


def remove_duplicados(lista_a, lista_b):
    """Remove itens duplicados"""
    primeira_lista = set(lista_a)
    segunda_lista = set(lista_b)
    return primeira_lista | segunda_lista


def main():
    """Função principal definidora do fluxo do programa"""
    prime_numbers = abre_arquivo('dados/primenumbers.txt')
    happynumbers = abre_arquivo('dados/happynumbers.txt')

    prime_numbers = transforma_em_lista(prime_numbers)
    happynumbers = transforma_em_lista(happynumbers)

    lista_final = remove_duplicados(prime_numbers, happynumbers)
    return sorted(lista_final)


if __name__ == "__main__":
    print(main())
