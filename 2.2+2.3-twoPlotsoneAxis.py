import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01) #from, to, increment
#range works with int only while arrange works also with floats etc
y = 3.0 * x
noise = np.random.normal(0.0, 1.0, len(x)) 

plt.plot(x, y + noise, 'g.', label="Actual Data") 
plt.plot(x, y, 'b-',label="Fitted Model")


plt.title("Average Speed vs. Distance Covered Over Time")
plt.xlabel("Average Speed (km/h)")      # Remember Units!
plt.ylabel("Distance Covered (km)")
plt.legend()

plt.show()