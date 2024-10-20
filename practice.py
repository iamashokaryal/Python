class Animal:

    def eat(self):

        print('I can eat food')

class Dog(Animal):

    def bark(self):
        print('I can Bark')

doggy = Dog()

doggy.eat()