"""
@author: vinimmelo

Select smaller word in a list.
"""

def menor_nome(lista):
    menor = len(lista[0].strip())
    novinha = lista[0].strip()
    for palavra in lista:
        new = palavra.strip()
        if len(new)<menor:
            menor = len(new)
            novinha = new
    return novinha.capitalize()
