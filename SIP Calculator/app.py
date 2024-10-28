print('<------- WELCOME TO SIP CALCULATOR ------->')

class Sip:

    def sip_calculate(self,amount,years,dividend):
        self.amount = amount
        self.years = years
        months = years * 12
        self.dividend = dividend

        for i in range(1,self.years):

            self.amount = self.amount + (self.amount*dividend)/100
            
        return self.amount


amount = int(input('Enter the amount you want to invest: \n'))

years = int(input("For how many years? \n"))

dividend = int(input("How much return do you expect? \n"))

sip = Sip()

result = sip.sip_calculate(amount,years,dividend)

print(result)







        