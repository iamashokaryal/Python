# First letter of class is capital

class Bike:

    def full_name(self):
        self.brand = 'Pulsar'
        self.model = 'NS'
        return f"{self.brand}"

my_bike = Bike()
print(my_bike.full_name)
