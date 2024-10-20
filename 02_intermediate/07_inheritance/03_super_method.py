
# It is possible to call the base class from derived classes
# For that we use super()


# Base class
class Polygon:

    def __init__(self,sides):

        self.sides= sides
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter  = sum(self.sides)
        return perimeter

#derived class
class Triangle(Polygon):
    def display_info(self):
    # call the display_info() method of Polygon

        super().display_info()

#Creating Object of Triangle 
t1 = Triangle([5,6,7])

# Call get_perimeter() using object t1
perimeter = t1.get_perimeter()


print('Perimeter:', perimeter)

# call display_info() using t1

t1.display_info() 