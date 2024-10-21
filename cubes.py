# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5,000 cubic numbers.

#15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

limit = 50001

x_values = range(1,limit)
y_values = [x**3 for x in x_values]


plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap = plt.cm.Wistia, s=5)

ax.set_title("Cubic numbers", fontsize = 20)
ax.set_xlabel("Values", fontsize = 10)
ax.set_ylabel("Cubes", fontsize = 10)
ax.tick_params(labelsize = 8)

plt.show()