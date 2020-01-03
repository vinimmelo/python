#!/usr/bin/env python3
from collections import UserDict


class DoppelDict(UserDict):
    """
    Class to illustrate the problem of inheritance of buil in types in Python
    """

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
