
def busca(lista, elemento):
    inicio = 0
    fim = len(lista)-1
    meio = fim//2
    if meio==elemento:
        return meio
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(meio)
        if elemento == lista[meio]:
            return meio
        else:
            if elemento<lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    return False
