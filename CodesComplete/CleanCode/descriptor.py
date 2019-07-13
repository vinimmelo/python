class NonDataDescriptor:
    def __get__(self, instance, value):
        if instance is None:
            return self
        print('Descriptor test!')
        return 42


class DataDescriptor:
    def __get__(self, instance, value):
        if instance is None:
            return self
        print('Descriptor test!')
        return 42
    def __set__(self, instance, value):
        print('Setting descriptor')
        instance.__dict__["descriptor"] = value


class Dog:
    descriptor = DataDescriptor()
    def __init__(self, legs, eyes):
        self.legs = legs
        self.eyes = eyes

    def bark(self):
        return f"Legs: {self.legs} Eyes: {self.legs}"

