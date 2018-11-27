# -*- coding: utf-8 -*-
"""
Created on Oct 11

@author: vinimmelo

Main test Archive
"""

from random import randint
import itertools
import pandas

messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def do_too_many_things(listinha: list):
    coisa_feia = listinha.pop()
    listinha.append('and ' + coisa_feia)
    return str(', '.join(listinha))


def revert_lists(listinha: list):
    eixo_x = len(listinha)
    eixo_y = len(listinha[0])
    for y in range(eixo_y):
        for x in range(eixo_x):
            print(listinha[x][y], end=' ')
        print()


def displayInventory(inventory):
    print("Inventory:")
    sum = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        sum += v
    print("Total numbers of items: " + str(sum))

def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
