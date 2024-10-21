import pandas as pd

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Felipe', 'Rita'],
        'Age': [25, 30, 35, 40, 22, 29],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Bogota', 'Banglore']}
df = pd.DataFrame(data)

# rename column 'Name' to 'Name of Person'
df.rename(columns={'Name':'Name_of_Person'}, inplace= True)

print(df)