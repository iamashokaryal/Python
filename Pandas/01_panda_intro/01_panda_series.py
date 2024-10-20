import pandas as pd

data = [10,20,30,40,50,60,70,80,90]

my_series = pd.Series(data)

print(my_series)

# dtype: int64 denotes that the series stores the values of int64 types.

# Accessing value in series usnig labels

print(my_series[2])
