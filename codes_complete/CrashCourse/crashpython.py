"""
Created on 17 December 2018
@author vinimmelo
Training Module of Python Crash Course book!
"""

from collections import OrderedDict
from random import randint


def page_185():
    favorite_languages = OrderedDict()

    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c'
    favorite_languages['edward'] = 'ruby'
    favorite_languages['phil'] = 'python'

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " +
            language.title() + ".")
