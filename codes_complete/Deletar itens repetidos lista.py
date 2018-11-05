lista_teste = [1, 2, 10, 25, 15, 40, 2, 37]

def remove_repetidos(lista):
    lista = sorted(lista)
    y = 0
    cont = 1
    z = lista[1]
    for x in lista:
        if x==z:
            z = x
            lista.remove(x)
            cont += 1
        else:
            z = x
    return lista

print(remove_repetidos(lista_teste))