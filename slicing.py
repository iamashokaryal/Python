import pandas as pd

# create a categorical Series
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype="category")

# display the original categorical variable
print("Original Series:")
print(cat_series)

# remove specific categories
categories_to_remove = ["B", "C"]
cat_series_removed = cat_series.cat.remove_categories(categories_to_remove)

# display the modified categorical variable
print("Modified Series:")
print(cat_series_removed)