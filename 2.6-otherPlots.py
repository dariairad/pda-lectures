import matplotlib.pyplot as plt
import numpy as np

# scatter plot
x1 = np.random.uniform(0.0, 10.0, 100) 
x2 = np.random.uniform(0.0, 5.0, 100)
x3 = np.random.randint(0, 20, 100) #same as uniform but generates ints
x4 = np.random.normal(0.0, 10.0, 100)

plt.subplot(1, 2, 1) #columns, rows, index (indexed from 1)
plt.scatter(x1, x2, c=x3, s=x4) #x1, x2, colour, size

# generating functions
x5 = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)
plt.subplot(1, 2, 2)
plt.plot(x5, np.sin(x5), "g.")
plt.plot(x5, np.cos(x5), "b.")

plt.show()