class Student:

    def check_pass_fail(self):

        if self.score >=40:

            return True
        
        else:

            return False
        
student1 = Student()

student1.name = 'Harry'

student1.score = 85

did_pass = student1.check_pass_fail()

print(did_pass)