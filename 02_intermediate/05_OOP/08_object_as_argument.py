class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_person_attributes(self,person):

        print(self.name)
        print(self.age)
        print(person.name)
        print(person.age)

person1 = Person('Tina',22)

person2 = Person('Ramesh',23)
# calling print_persons_attributes() using person1 object
# person2 is used as an argument
person1.print_person_attributes(person2)

#The attributes of the person1 object is name which is equal to 'Tina' and age which is equal to 22.
#The attributes of the person2 object is name which is equal to 'Ramesh' and age which is equal to 23.
#Inside the print_persons_attributes(), self will be person1. It's because we have called this method using person1. And, the person argument takes the value of person2, which is passed as an argument.
#Now, when we print self.name and self.age, we get attributes of person1. And when we print person.name and person.age, we get attributes of person2.
