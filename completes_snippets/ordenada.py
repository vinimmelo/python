"""
@author: brmelovi

Verify if a list is ordened
"""

def ordenada(lista):
    new_lista = sorted(lista[:])
    if lista == new_lista:
        return True
    else:
        return False
