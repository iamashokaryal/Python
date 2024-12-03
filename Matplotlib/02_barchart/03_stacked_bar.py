import matplotlib.pyplot as plt
import pandas as pd

# Load the data
medals = pd.read_csv("Matplotlib/src/csv/medals.csv", index_col=0)

# print(medals.columns)

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the bars
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

# Add a legend
ax.legend()

# Show the plot
plt.show()
