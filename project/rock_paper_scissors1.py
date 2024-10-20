import random
class Game:

    def __init__(self):
        self.computer_pick = self.get_computer_pick()
        self.user_input = self.get_user_pick()

        self.result = self.get_result()

    def get_computer_pick(self):
        random_number = random.randint(1,3)

        options = {1:'rock', 2:'paper',3:'scissors'}

        computer_pick = options[random_number]

        return computer_pick
    
    def get_user_pick(self):
        while True:
            user_input = input("Enter rock/paper/scissors:")
            user_input.lower()
            return user_input
            
            if user_input in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Wrong input')
        return user_input
    
    def get_result(self):
        if self.computer_pick == self.user_input:
            return 'Draw !!'
        elif self.computer_pick =='rock' and self.user_input=='paper':
            return 'You Win, Computer Lost' 
        elif self.computer_pick =='paper' and self.user_input=='scissors':
            return 'You Win, Computer Lost'
        elif self.computer_pick =='scissors' and self.user_input=='rock':
            return 'You Win, Computer Lost'
        else:
            return 'Computer Win, You Lost!'
    
    def print_result(self):
        print(f'Computers pick : {self.computer_pick}')
        print(f'Yours pick : {self.user_input}')
        print(f'Result : {self.result}')
while True:
    game = Game()
    game.print_result()
    play_again = input('Do you want to play again (y/n):')

    if  play_again != 'y':
        break


              

        
        
