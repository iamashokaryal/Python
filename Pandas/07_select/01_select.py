import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 27, 29],
    'Salary': [50000, 60000, 45000, 55000, 52000]
}

df = pd.DataFrame(data)

# select a single column 
name_column = df['Name']

print("Selecting the column 'Name':")

print(name_column)

# selecting multiple columns 

mul_col = df[['Age','Salary']]

# This gives result without index
print(mul_col.to_string(index=False))

# this gives result with index

print(mul_col)


# select rows using slicing

selected_rows = df[1:4]

print(selected_rows)