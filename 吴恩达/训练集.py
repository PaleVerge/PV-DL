import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0,2.0,3.0])
y_train = np.array([10,20,30])
z_train = np.array([[1,1,1],[2,2,2]])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

print(f"z_train = {z_train}\n")

print(f"x_train_shape = {x_train.shape}")
print(f"dimension of z_train = {len(z_train.shape)}")  ## z的维度数量
print(f"z_train_shape = {z_train.shape}\n")

print(f"number of x_train = {x_train.shape[0]}") ## x_train第 0 维的大小
print(f"number of x_train = {len(x_train)}")  ## x_train第 0 维的大小
print(f"number of z_train = {z_train.shape[1]}") ## z_train第 1 维的大小

plt.scatter(x_train, y_train, marker='x',c='r')
plt.title("Housing Prices")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
