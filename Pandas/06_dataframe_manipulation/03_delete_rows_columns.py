import pandas as pd

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Felipe', 'Rita'],
        'Age': [25, 30, 35, 40, 22, 29],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Bogota', 'Banglore']}
df = pd.DataFrame(data) 

print('Original dataframe: \n \n',df,'\n')

# delete rows with index 4

df.drop(index=4, inplace= True)

# delete rows with index 5
df.drop(5, axis=0, inplace=True)

df.drop([2,3], inplace=True)

# delete Column

df.drop('Name',axis=1, inplace=True)

print('After Drop: \n \n',df)




