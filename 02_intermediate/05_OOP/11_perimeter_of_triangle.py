
class Triangle:

    def __init__(self,a,b,c):
        self.s1 = a
        self.s2 = b
        self.s3 = c

    def get_perimeter(self):
        perimeter = self.s1+self.s2+self.s3

        return perimeter

a= int(input())

b= int(input())

c= int(input())

t1 = Triangle(a,b,c)

result = t1.get_perimeter()

print('Perimeter of Triangle :',result)

