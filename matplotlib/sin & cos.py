import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x=np.arange(-5,5,0.1)
y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,ls=":",label="cos")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sin & Cos Function")

plt.legend()
plt.show()