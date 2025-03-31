class Animals():
    def __init__(self, breed):
        self.breed = breed

    def sound(self):
        print(f'Dog is {self.breed}) and it {self.sound}!')

class Dog(Animals):
    def sound(self):
        print(f'{self.breed} barks!')

class Cat(Animals):
    def sound(self):
        print(f'{self.breed} meow!')

dog = Dog('Rotweiller')
(dog.sound())

cat = Cat('Bebo')
(cat.sound())