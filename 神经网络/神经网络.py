import numpy as np

from 激活函数.Sigmoid_function import sigmoid
from 激活函数.Identity_function import identify_function

def init_network():
    network={}
    network['W1']=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['W2']=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['W3']=np.array([[0.1,0.3],[0.2,0.4]])

    network['B1']=np.array([0.1,0.2,0.3])
    network['B2']=np.array([0.1,0.2])
    network['B3']=np.array([0.1,0.2])
    return network

def forward(network,X):
    A1=np.dot(X,network['W1'])+network['B1']
    Z1=sigmoid(A1)
    A2=np.dot(Z1,network['W2'])+network['B2']
    Z2=sigmoid(A2)
    A3=np.dot(Z2,network['W3'])+network['B3']
    y=identify_function(A3)
    return y


network=init_network()
X=np.array([1.0,0.5])
y=forward(network,X)

print(y)


