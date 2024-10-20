class Person:

    def greet(self,message):
        self.message= message
        print(self.message)

greeting = input("Enter:")
person1 = Person()

person1.greet(greeting)


