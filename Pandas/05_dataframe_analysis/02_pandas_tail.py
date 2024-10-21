import pandas as pd 

data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}
df = pd.DataFrame(data)

# display the last 3 rows
print("Last three rows: \n")

print(df.tail(3),'\n')

print('Last five rows: \n')
print(df.tail())