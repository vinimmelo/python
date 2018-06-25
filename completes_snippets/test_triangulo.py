from unittest import TestCase
from completes_coursera.triangulo2 import *

a = Triangulo(1, 2, 3)
b = Triangulo(2, 4, 6)
c = Triangulo(4, 8, 12)
d = Triangulo(3, 4, 5)
e = Triangulo(2, 2, 2)

class TestTriangulo(TestCase):
    def test_perimetro(self):
        self.assertEqual(a.perimetro(), 6)

    def test_tipo_lado(self):
        self.assertEqual(a.tipo_lado(), 'escaleno')
        self.assertEqual(e.tipo_lado(), 'equilátero')

    def test_retangulo(self):
        self.assertFalse(a.retangulo())
        self.assertTrue(d.retangulo())


if __name__ == '__main__':
    TestTriangulo()