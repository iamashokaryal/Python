from matplotlib import pyplot as plt

x = [1,2,3,4,5]

y = [3,6,8,9,10]

a= [2,3,5,7,8]

b = [3,7,3,8,3]
# Add the title
plt.title("MY DATA")

# set x and y labels
plt.xlabel("X axis.")

plt.ylabel("Y axis.")

plt.plot(x,y,label= "First line", marker= 'v',linestyle= '--',color = 'r')

plt.plot(a,b,label= 'Second Line', marker= 'o',linestyle = '--',color='g')

plt.legend()

# Display the figure

plt.show()