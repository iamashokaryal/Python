
name = input('What is your name? \n')

message = input('Status of day, Morning/Afternoon/Evening: \n').lower()

if message == 'morning':
    print(f'Good Morning {name}!')
elif message == 'afternoon':
    print(f'Good Afternoon {name}!')
elif message == 'evening':
    print(f'Good Evening {name}!')

else:
    print('Wrong input !!')
