import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
print('Original Dataframe:')
print(df)

# inplace is by default False, so we need to change to True
# This is useful when you want to avoid unnecessary copies of large datasets 
# and just want to make changes directly.

df.rename(index={0:'A',1:'B',2:'C'}, inplace=True)
print('Modified Dataframe:')

print(df)

# reset index
df.reset_index(inplace=True)

print('After Reset:')

print(df)