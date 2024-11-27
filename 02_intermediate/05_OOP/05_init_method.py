class Student:
    # adding the __init__() method
    def __init__(self,name,score):
        self.name = name
        self.score = score
    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score>=40:
            return True
        else:
            return False
        
#creating object

student1 = Student('Harry', 85)

did_pass = student1.check_pass_fail()

# calling this method using student1
print(student1.name,'pass?', did_pass)

print(f'Did {student1.name} pass?', did_pass)



