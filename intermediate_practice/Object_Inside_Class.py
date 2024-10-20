class Engine:

    def __init__(self,power):
        self.power = power


class Vehicle:

    def __init__(self,wheels):
        self.wheels = wheels

        self.engine = Engine(400)

        
        

    def get_power(self):
        a= self.engine.power
        print(a)

vehichle = Vehicle(4)

vehichle.get_power()




        

    

    