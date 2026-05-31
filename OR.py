def OR(x1,x2):
    w1,w2,theta=0.5,0.5,0
    tmp=w1*x1+w2*x2
    if(tmp<=theta):
        return 0
    else:
        return 1
print("1 OR 1 =",OR(1,1))
print("0 OR 1 =",OR(0,1))
print("1 OR 0 =",OR(1,0))
print("0 OR 0 =",OR(0,0))