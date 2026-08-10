import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin") ## 图例标签
plt.plot(x,y2,ls=":",label="cos")

plt.xlabel("x") ## x轴标签
plt.ylabel("y") ## y轴标签
plt.title("Sin & Cos Function") ## 标题

plt.legend() ## 显示图例
plt.show() ## 绘图