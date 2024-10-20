
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
        print("A triangle is a polygon with 3 edges.")

#Creating Object of Triangle 
t1 = Triangle([5,6,7])

# Call get_perimeter() using object t1
perimeter = t1.get_perimeter()


print('Perimeter:', perimeter)

# call display_info() using t1

t1.display_info() # base ra derived class maa same method(name same) xa vane derived class le base class ko method lai
                  #override garxa ra derived class ko method maatra call hunxa !



# This code t1.display_info() class the display_info() method. However, both Polygon and Triangle have this method. 
# In such cases, the display_info() method of the derived class Triangle is called and the method of the base class Polygon is ignored.
# This is called method overriding.

# If the same method is defined in both the base and the derived class, 
# then the method of the derived class overrides the method of the base class.