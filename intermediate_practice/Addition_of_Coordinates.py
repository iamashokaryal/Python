class Coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add_coordinates(self,cor):

        result1 = self.x +cor.x
        result2 = self.y + cor.y
        corr = Coordinate(result1, result2)
        return corr
c1 = Coordinate(5,6) 
c2 = Coordinate(7,9)

c3 = c1.add_coordinates(c2)

print(c3.x)

print(c3.y)