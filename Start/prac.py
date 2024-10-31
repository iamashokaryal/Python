class Sum:

    def compute_sum(self,a,b):
        self.num1 = a
        self.num2 = b
        self.sum = self.num1 + self.num2       
        
    
    def print_sum(self):

        print(self.sum)

a = int(input('Enter first Value: \n')) 
b = int(input('Enter Second Value: \n'))

sum = Sum()

sum.compute_sum(a,b)

sum.print_sum()

