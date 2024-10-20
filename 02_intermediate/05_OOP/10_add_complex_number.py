

class Complex:

    def __init__(self,real,imag):
        self.real = real

        self.imag = imag

    def add(self,number):  #here self = n1 & number = n2
        real_result = self.real+number.real
        #real result = 4+6

        imaginary_result = self.imag + number.imag
        #imaginary result = 6+2
        result = Complex(real_result,imaginary_result) #aba yesle constructor clal garxa
        return result # this return the object and goes to n3




n1 = Complex(4,6)
n2 = Complex(6,2)

n3= n1.add(n2)

print('real part=',n3.real)

print('Imaginarypart =',n3.imag)