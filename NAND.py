def NAND(x1,x2):
    w1,w2,theta=0.5,0.5,0.8
    tmp=w1*x1+w2*x2
    if(tmp<=theta):
        return 1
    else:
        return 0
print("1 NAND 1 =",NAND(1,1))
print("0 NAND 1 =",NAND(0,1))
print("1 NAND 0 =",NAND(1,0))
print("0 NAND 0 =",NAND(0,0))