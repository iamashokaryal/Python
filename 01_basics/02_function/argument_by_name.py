
#In python we can pass argument to the function not only based on the postion, we can also pass
#argument by name

def greet(name, address):
    print("my name is",name, 'and i live in', address,".")

greet('Hari', 'Kathmandu') #passed based in postion

greet(address='Butwal', name='Ashok Aryal')  #pass argument by name