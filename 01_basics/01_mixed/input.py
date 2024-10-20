num = input('Enter the number: ')

print('You have just Entered: ', num)

print('Data Type of yout entered number is: ', type(num))

#It is important to note that the entered value 10 is a string, not a number. So, type(num) returns <class 'str'>.
#To convert user input into a number we can use int() or float() functions as:

num1 = int(input('Enter a number1:'))
num2 = int(input('Enter a number2:'))

sum = num1+ num2
multiply = num1*num2

print('Sum is:', sum)
print('Multiplication is:', multiply)

