import copy
import numpy as np
import math

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

def gradient_descent(x,y,w_init,b_init,alpha,num_iters):

    w = copy.deepcopy(w_init)   ## 防止修改全局
    b = copy.deepcopy(b_init)

    J_history = []
    P_history = []

    for i in range(num_iters):
        gradient_w,gradient_b = compute_gradient(x,y,w,b)
        w -= alpha * gradient_w
        b -= alpha * gradient_b
        if i < 100000:
            J_history.append(compute(w,x[i],b))
            P_history.append([w,b])

        if i% math.ceil(num_iters/10) == 0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {gradient_w: 0.3e}, dj_db: {gradient_b: 0.3e}  ",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")

    return w , b , J_history , P_history

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
w_init = 0
b_init = 0

iterations = 10000
tmp_alpha = 1.0e-2

w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha,
                                                    iterations)
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")
