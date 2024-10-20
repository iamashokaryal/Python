import pandas as pd

# create dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# set the 'Name' column as index

df.set_index('Name', inplace=True)

# create range index
df1 = pd.DataFrame(data, index= pd.RangeIndex(5,8, name= 'Index'))

                   

print(df)
print('-----------------------------------------')
print(df1)

