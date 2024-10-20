import random
def compute_random():

    random_number = random.randint(1,3)

    options = {1:'rock', 2: 'paper', 3:'scissors'}

    computer_choice = options[random_number]
    return computer_choice

def get_user_input():

    user_input = input("Choose rock/paper/scissors:")
    user_input.lower()
    return user_input

def get_result(computer_inputs,user_inputs):

    if computer_inputs == user_inputs:
        return 'draw'
    elif computer_inputs =='rock' and user_inputs =='paper':
        return 'You win!'
    elif computer_inputs =='paper' and user_inputs =='scissors':
        return 'You win!'
    elif computer_inputs =='scissors' and user_inputs =='rock':
        return 'You win!'
    else:
        return "You Lost!"
    
computer_input = compute_random()

user_input = get_user_input()

result = get_result(computer_input,user_input)

print('Computer choice:',computer_input)
print('Your choice:',  user_input )
print('result:', result)
    

