"""
Just a simple code to inspect function and signatures...
"""

from tag import tag

import inspect

def hello(teste, teste2, uow) -> 'int > 1':
    pass


if __name__ == '__main__':
    sig = inspect.signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    print(sig)

    bound_args = sig.bind(**my_tag)
    print(bound_args)

    sig2 = inspect.signature(hello)
    print(sig2)
    print(sig2.return_annotation)
