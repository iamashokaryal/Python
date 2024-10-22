import pandas as pd

data = {
    'Name':['Jhethalal','Bhide','Popatlal','Dr.Hathi'],
    'Age':[43,42,35,40],
    'Job':['Businessman','Teacher','Journalist','Doctor'],
    'Salary':[1000000,70000,55000,120000]

}

df = pd.DataFrame(data)
# sorting by single variable in ascending order
df = df.sort_values('Salary')

print('Sorting in ascending: \n',df)
# sorting in descending order
df = df.sort_values('Salary', ascending = False)

print('Sorting in descending order: \n',df)

# sorting by multiple variables

df = df.sort_values(['Name','Salary'],ascending=[True,False])

print(df)