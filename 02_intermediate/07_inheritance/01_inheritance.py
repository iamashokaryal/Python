#Base Class
class Animal:
    
    def eat(self):
        print('I am eating.')

# The dog class is derived from Animal
class Dog(Animal):

    def bark(self):
        print("I am a dog, Obviously i can bark.")

# The Dog class inherits all the attributes and methods from the Animal class. 
# But what does that mean?

# It means, objects of the Dog class can not only access methods 
# and attributes of the Dog class, but it can also access methods and attributes of the Animal class.
class Cat(Animal):
    def sounds(self):

        print("Meow!")


#object of the dog class
dog1 = Dog()

# call the bark() method of class child class Dog
dog1.bark()

# call the eat() method of base class Dog
dog1.eat()

#object of cat class
cat1 = Cat()

cat1.eat()
cat1.sounds()