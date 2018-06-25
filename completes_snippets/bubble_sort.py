def bubble_sort(lista):
    for x in range(len(lista)-1, 0, -1):
        for j in range(x):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista
