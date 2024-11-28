from matplotlib import pyplot as plt 
import numpy as np

# np.linspace(start, stop, num=100)
# Generates 100 evenly spaced points between 0 and 10, inclusive.

x = np.linspace(0, 10, 100)

a = np.sin(x)

b = np.cos(x)

# # Create a 2x1grid of subplots
fig, ax = plt.subplots(2,2, figsize=(10, 8))

# First subplot

ax[0,0].plot(x,a,color = 'red')
ax[0,0].set_title("Sine Function.")
ax[0,0].set_xlabel("X")
ax[0,0].set_ylabel("Sin(x  )")

# second subplot

ax[0,1].plot(x,b,color='green')
ax[0,1].set_title("Cos Function.")
ax[0,1].set_xlabel("X")
ax[0,1].set_ylabel("Cos(x)")

# Adjust layout to prevent overlapping

plt.tight_layout()


plt.show()