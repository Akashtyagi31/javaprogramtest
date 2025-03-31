class Bird():
    def speak(self):
        print("Chirping Chirping!!!")

class Cat():
    def speak(self):
        print("Meow Meow!!!")

Animals = [Bird(),Cat()]
for Animal in Animals:
    Animal.speak()
