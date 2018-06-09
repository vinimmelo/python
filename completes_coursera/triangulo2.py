class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            maior = self.a
            num1 = self.b
            num2 = self.c
        elif self.b > self.a and self.b > self.c:
            maior = self.b
            num1 = self.a
            num2 = self.c
        else:
            maior = self.c
            num1 = self.b
            num2 = self.a
        if (maior**2) == (num1**2) + (num2**2):
            return True
        else:
            return False

