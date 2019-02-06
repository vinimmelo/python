"""
Simply decorators and inner functions training.
Created on 05 February 2019
@vinimmelo - Vinícius Melo
"""

def multiply(n):
    def inner_multiplication(x):
        return x * n
    return inner_multiplication


for_three = multiply(3)
print(for_three(5))
print(for_three(10))

for_five = multiply(5)
print(for_five(5))
print(for_five(7))


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def whee():
    print('Wheee!')


whee()
