import numpy as np
import matplotlib.pylab as plt

def step_function(x):
   y=x>0
   return y.astype(int)
x=np.arange(-5,5,0.1)
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
n1=np.array([-3,-2,-1,0,1,2,3])
print(n1)
n2=step_function(n1)
print(n2)