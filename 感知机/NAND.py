import numpy as np
def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.8
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1
print("1 NAND 1 =",NAND(1,1))
print("0 NAND 1 =",NAND(0,1))
print("1 NAND 0 =",NAND(1,0))
print("0 NAND 0 =",NAND(0,0))