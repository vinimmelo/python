import random
from tombola import Tombola

class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)
    # TODO: finalizar
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()
