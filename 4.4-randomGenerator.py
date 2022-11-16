import numpy as np
import matplotlib.pyplot as plt

#[inclusive 
#(exclusive

rng = np.random.default_rng()
# x = rng.random((5, 4)) #5 rows, 4 columns
# print(x)

y = rng.random (1000000)
plt.hist(y)
plt.show()

