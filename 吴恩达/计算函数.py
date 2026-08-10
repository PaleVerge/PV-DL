import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0,2.0,3.0])
w = 100
b = 100

y_train = np.array([100,200,300])

def compute(w,x,b):
    m=len(x)
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

    return f_wb

plt.scatter(x_train, y_train, marker='x',c='r',label='Actual Data')
plt.plot(x_train,compute(w,x_train,b),label='Prediction')
plt.title("Housing Prices")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
