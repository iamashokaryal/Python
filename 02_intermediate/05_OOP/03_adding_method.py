class Student:
        # add a method to check pass/fail

    def check_pass_fail(self):
        if self.score >=50:
            return True
        
        else:
            return False
# create object   
Student1 = Student()

Student1.name = 'Harry'
Student1.score = 85

# calling this method using student1 object
did_pass = Student1.check_pass_fail()

print(f'{Student1.name} pass?', did_pass)