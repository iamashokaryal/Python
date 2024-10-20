class Squre:

    def __init__(self,length):
        self.length= length

    def compute_area(self):
        area = self.length**2
        return area
    def compute_perimeter(self):
        perimeter = self.length * 4

        return perimeter
    
length = int(input('Enter the length of the squre :'))

sq = Squre(length)

area = sq.compute_area()

perimeter = sq.compute_perimeter()

print(area)
print(perimeter)

    