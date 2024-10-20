#define function

def addition(c,d):
    sum = c+d
    print('sum is:',sum)

def subtract(c,d):
    difference = c-d
    print('Difference is:',difference)

def multiplication(c,d):
    mul = c*d
    print('multiplication is:',mul)

def division(c,d):
    div = c/d
    print('division is:',div)

a= int(input('Enter the first number:'))
b= int(input('Enter the value of second number:'))

#function call
addition(a,b)
multiplication(a,b)
subtract(a,b)
division(a,b)
