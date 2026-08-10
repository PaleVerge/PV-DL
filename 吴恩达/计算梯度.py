import numpy as np

def compute(w,x,b):
    m=len(x)
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

    return f_wb

def cost_function(x,y,w,b):
    m = len(x)
    cost_sum = 0

    for i in range(m):
        f_wb = compute(w,x,b)
        cost = (f_wb-y[i]) ** 2
        cost_sum += cost
    j = cost_sum / (2 * m)

    return j

def compute_gradient(x,y,w,b):
    m = len(x)
    gradient_b= 0
    gradient_w = 0

    for i in range(m):
        f_wb = compute(w,x,b)
        gradient_w += (f_wb[i] - y[i]) * x[i]
        gradient_b += (f_wb[i] - y[i])
    gradient_w /= m
    gradient_b /= m

    return gradient_w,gradient_b

