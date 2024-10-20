class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def return_another_person(self):

        person1 = Person('Sara', 20)

        return person1
    
person1 = Person('Ana', 20)

another_person = person1.return_another_person()

print(another_person.name)
print(another_person.age)
