def busca(lista, elemento):
    i = 0
    for x in lista:
        if elemento is x:
            return i
        i += 1
    return False