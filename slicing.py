
student_marks = [20,30,40,50,60,70,80,90]

pass_student_marks = [marks for marks in student_marks if marks>50]


pass_student_avg = sum(pass_student_marks)/len(pass_student_marks)

print('Avg',pass_student_avg)

print(pass_student_marks)

