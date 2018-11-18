"""
@author: vinimmelo

Insertion Sort
"""
def insertion_sort(lista):
    nova_lista = []
    for x in lista:
        if x==lista[0]:
            nova_lista.append(x)
        else:
            for i in range(len(nova_lista)):
                if x <= nova_lista[i]:
                    nova_lista.insert(i, x)
                    break
                elif x > nova_lista[i] and i == len(nova_lista) - 1:
                    nova_lista.append(x)
    return nova_lista
