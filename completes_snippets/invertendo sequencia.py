"""
@author: brmelovi

Inverting Sequence
"""

usuario = int(input("Digite uma sequencia de numeros terminada por 0: "))
lista1 = []
while not usuario==0:
    lista1.append(usuario)
    usuario = int(input("Digite uma sequencia de numeros terminada por 0: "))

cont = len(lista1)
z = 0
x = -1
while z < cont:
    print(lista1[x])
    x -= 1
    z += 1
