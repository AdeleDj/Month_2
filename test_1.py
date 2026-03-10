class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print('Animal makes sound')


class Dog(Animal):
    def make_sound(self):
        print('Woof-woof!')


class Cat(Animal):
    def make_sound(self):
        print('Meow-meow!')


dog = Dog('Luana', 8)
kitty = Cat('Rusty', 6)

dog.make_sound()
kitty.make_sound()

kitty.set_age(2)
print(kitty.get_age())