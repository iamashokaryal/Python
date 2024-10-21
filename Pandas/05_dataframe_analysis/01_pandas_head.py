import pandas as pd

data =  {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}
df = pd.DataFrame(data)

# display the first three rows
print('First three rows: \n')

print(df.head(3),'\n')

# display first five rows
print('First five rows: \n')
print(df.head())