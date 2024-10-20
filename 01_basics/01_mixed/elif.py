marks = int(input('Enter your marks:'))

if marks>100 or marks<0:
    print("invalid garde")

elif marks>=40:
    print('You have passed.')

else:
    print('you have been failed.')