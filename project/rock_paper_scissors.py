import random

def get_cmp_choice():
    random_number = random.randint(1,3)

    options = {1:'rock', 2:'paper', 3:'scissors'}

    computer_choice = options[random_number]

    return computer_choice

def get_user_input():

    user_input = input('Enter rock / paper /  scissors:')

    user_input = user_input.lower()

    return user_input

def get_result(user_pick, computer_pick):

    if user_pick == computer_pick:
        return 'draw'
    elif user_pick == 'paper' and computer_pick == 'rock':
        return 'win'
    elif user_pick == 'rock' and computer_pick == 'scissors':
        return 'win'
    elif user_pick == 'scissors' and computer_pick =='paper':
        return 'win'
    
    else:
        return 'lose'
    
comupters_pick = get_cmp_choice()

users_pick = get_user_input()

result = get_result(users_pick, comupters_pick)

print("Computer's pick:", comupters_pick )

print("Your pick:", users_pick)

print('You', result, "!")

