
class Buy:

    def price_input(self):

        self.item_prices = []

        self.no_of_item = int(input("Enter the no of items: \n"))

        for i in range(1,self.no_of_item+1):

            price = int(input(f"Enter item {i} price: \n"))

            self.item_prices.append(price)

        
    def price_calculation(self):

        self.total_amount = sum(self.item_prices)


    def print_result(self):
        print(f"Prices ares : {self.item_prices}")
        print(f"The amount you need to pay is : {self.total_amount}")

buy = Buy()

buy.price_input()

buy.price_calculation()

buy.print_result()

        