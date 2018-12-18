"""
Created on 17 December 2018
@author vinimmelo
Simple dice Class.
"""
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(f"The dice of {self.sides} sides, rolls the number: {roll}")


if __name__ == '__main__':
    dice6 = Die()
    dice10 = Die(sides=10)
    dice20 = Die(sides=20)

    for x in range(10):
        dice6.roll_die()
        dice10.roll_die()
        dice20.roll_die()
