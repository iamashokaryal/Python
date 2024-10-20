import pandas as pd

# create dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# We can access rows of a DataFrame using the .iloc property. For example,

second_row = df.iloc[1]

print(second_row)