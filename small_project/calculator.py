print("<--------WELCOME TO MY CALCULATOR------------> \n")
class Calculate:

    def calculate_sum(self,num1,num2):

        sum = num1+num2

        return sum    
    
    def calculate_difference(self,num1,num2):

        diff = num1-num2

        return diff

    def calculate_multiplication(self,num1,num2):
        multiplication = num1*num2

        return multiplication

    def calculate_division(self,num1,num2):
        divison = num1/num2

        return divison
next_choice = 'yes'
while next_choice == 'yes':
    choice = input('Define operation you want to perform: \neg, +,-,*,/ \n').lower ()

    num1 = int(input('Enter first number: \n'))
    num2 = int(input('Enter second number: \n'))
    calc = Calculate()
    if choice == 'sum' or choice == '+':
        res = calc.calculate_sum(num1,num2)
        print(f'Sum of {num1} and {num2} is {res}.')

    elif choice == 'multiply' or choice == '*':
        res = calc.calculate_multiplication(num1,num2)
        print(f'Multiplication of {num1} and {num2} is {res}.')

    elif choice == 'divide' or choice =='/':

        res = calc.calculate_divisio+(num1,num2)
        print(f'Divison of {num1} and {num2} is {res}.')

    elif choice == 'substract' or choice == '-':

        res = calc.calculate_difference(num1,num2)
        print(f'Substraction {num1} and {num2} is {res}.')

    else:
        print('Wrong input!')

    next_choice = input('Do you want to calculate again ? yes/no \n')

print("<-----------Terminating----------------->")
print('''.
.
.
.
.
.
.
.''')
print('<------------Terminated-------------->')