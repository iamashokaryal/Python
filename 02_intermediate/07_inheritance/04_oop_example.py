class Person :
    def __init__(self,student_id):

        self.id = student_id

    def display_info(self):

        print(f'name:{self.name} and age is {self.age}')

class Student(Person):

    def display_info(self):
        
        print(f'name:{self.student_id}')
        super().Person()



student = Student(12)

student.display_info