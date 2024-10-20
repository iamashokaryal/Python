

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_of_marks = sum_of_marks / total_subjects
    return average_of_marks

def find_grade(average_of_marks):
    if average_of_marks>=80:
        grade = 'A'
        
    elif average_of_marks>=60 and average_of_marks<80:
        grade = 'B'
        
    elif average_of_marks>=50 and average_of_marks<60:
        grade = 'C'
        
    else:
        grade = 'F'
    return grade

marks = [55,64,75, 80, 65]
average_of_marks = find_average_marks(marks)
print('Average of Marks:', average_of_marks)

grade = find_grade(average_of_marks)
print("your grade is :", grade)