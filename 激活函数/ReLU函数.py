import numpy as np
def ReLU(x):
    return np.maximum(x,0)
print(ReLU(-5))