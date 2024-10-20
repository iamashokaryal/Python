import pandas as pd

# create a dictionary
grades = {'sem1': 3.25, 'sem2':3.58, 'sem3':3.80}

# create a series from dictionary
my_series = pd.Series(grades)

print(my_series)

print(my_series['sem1'])

# select specific dictionary items using index argument
my_series1 = pd.Series(grades, index = ['sem1','sem2'])

print(my_series1)