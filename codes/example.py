import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1,1,101)
y = x*x
plt.figure()
plt.plot(x,y)
plt.show()