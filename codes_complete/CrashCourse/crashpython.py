class Dog():
    """ A Simple atempt to model a dog. """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

    def __str__(self):
        return f"{self.name} has {self.age} years old!"


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called by the name: {self.restaurant_name}\n" +
              f"And the cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        print('The restaurant is open!')
