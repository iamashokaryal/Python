import pandas as pd

# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# return index object
print(df.index)

# return index values
print(df.index.values)