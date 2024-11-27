from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8,9]

y = [1,3,5,7,9,11,13,15,17]

x1 = [1,3,5,7,9,2,4,6,8]

y1 = [2,5,3,7,1,6,4,8,9]

plt.plot(x,y, label='First Line')

# linewidth is used to increase the width of the line
plt.plot(x1,y1, label = 'Second Line',linewidth=5)  

# to show the label we need to call this method
plt.legend()

plt.title("MY DATA")
plt.show()