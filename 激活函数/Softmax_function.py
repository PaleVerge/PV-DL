import numpy as np

def softmax_function(a):
    c=np.max(a)##防止溢出
    exp_a=np.exp(a-c)##防止溢出
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

a=np.array([0.3,2.9,4.0])
print(softmax_function(a))
print(np.sum(softmax_function(a)))
##softmax函数值域为0-1，和为1