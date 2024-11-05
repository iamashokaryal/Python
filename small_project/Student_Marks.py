class Student:
    def student_marks_input(self):
        self.student_marks = []


        no_of_student = int(input("Enter the no of students: \n"))

        for i in range(1,no_of_student+1):

            marks = int(input(f'Enter student {i} marks: \n'))

            self.student_marks.append(marks)

    def student_marks_calculation(self):

        self.average_marks = sum(self.student_marks)/len(self.student_marks)
        
        self.highest_marks = max(self.student_marks)

        self.lowest_marks = min(self.student_marks)


    def student_marks_print(self):

        print(f'Marks are {self.student_marks}')

        print('<---------------------------------------->')

        print(f'Average marks of student = {self.average_marks}.')

        print('<---------------------------------------->')


        print(f'Highest marks = {self.highest_marks}.')

        print('<---------------------------------------->')
        print(f'Lowest marks = {self.lowest_marks}.')

        print('<---------------------------------------->')



student = Student()
student.student_marks_input()
student.student_marks_calculation()
student.student_marks_print()


        

