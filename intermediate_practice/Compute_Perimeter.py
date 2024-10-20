
# create the Triangle class
class Triangle:
    # define the __init__() method
    def __init__(self, x,y,z):

        self.x = x
        self.y = y
        self.z = z

    # define the get_perimeter() method
    def get_perimeter(self):

        perimeter = self.x+ self.y+self.z

        return perimeter


# take three integer inputs
a = int(input())
b = int(input())
c = int(input())

# create an object of the Triangle class
triangle1 = Triangle(a,b,c)

# call the get_perimeter() method
perimeter = triangle1.get_perimeter()

# print the perimeter
print(perimeter)