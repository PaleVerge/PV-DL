import torch
x=torch.empty(2,2)
print("x",x)

y=torch.zeros(3,3,dtype=torch.long)
print("y",y)

z=torch.rand(3,3,dtype=torch.float)
print("z",z)

a=torch.tensor([[3,4],[5,6]])
print("a1",a)
a=a.new_ones(2,2,dtype=torch.float)
print("a2",a)
a=torch.randn_like(a,dtype=torch.float64)
print("a3",a)
print(a.shape)