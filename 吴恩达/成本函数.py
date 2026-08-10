import numpy as np

def compute(w,x,b):
    m=len(x)
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

    return f_wb

def cost_function(w,x,b):
    m = len(x)
    sum = 0
    for i in range(m):
        sum += compute(w,x,b)
    j=sum/(2*m)
    return j