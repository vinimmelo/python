"""
@author: brmelovi

Multiplication of Matrix
"""

import math


def multiplicacao_matriz(a, b):
    c = [[0,0,0], [0,0,0], [0,0,0]]
    lin = len(a)
    col = len(a[0])
    for x in range(lin):
        for y in range(col):
            c[x][y] = a[x][y] * b[x][y]
    return print(c)


def raio() -> object:
    numero = math.pi
    rai = 10
    area = (rai**2)*numero
    return print(area)

if __name__ == '__main__':
    raio()
