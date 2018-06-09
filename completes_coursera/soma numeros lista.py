lista_teste = [1, 2, 10, 25, 15, 40, 2, 37]

def soma_elementos(lista):
    contador = 0
    for x in lista:
        contador = contador + x
    return contador

print(soma_elementos(lista_teste))