import numpy as np
import matplotlib.pylab as plt

def ReLU(x):
    return np.maximum(x,0)
print(ReLU(-5))

x=np.arange(-5,5,0.1)
y=ReLU(x)
plt.plot(x,y)
plt.ylim(-0.1,5)
plt.show()
