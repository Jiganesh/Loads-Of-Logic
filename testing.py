# importing the required module
import matplotlib.pyplot as plt

n =[[1, 59], [5, 6], [11, 63], [17, 29], [18, 2], [19, 65], [29, 73], [30, 32], [31, 68], [33, 9], [34, 25], [39, 8], [42, 71], [44, 97], [45, 3], [46, 77], [48, 86], [49, 94], [50, 27], [52, 20], [53, 63], [57, 81], [59, 9], [61, 57], [64, 49], [66, 91], [67, 13], [69, 29], [73, 20], [76, 91], [79, 23], [80, 69], [82, 61], [85, 7], [87, 91], [88, 49], [90, 51], [93, 56], [94, 50], [98, 37], [99, 69]]
x = [i[0] for i in n]
# corresponding y axis values
y = [i[1] for i in n]

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()