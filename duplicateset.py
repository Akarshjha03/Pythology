a=[1,2,10,20,40,80] #given in list
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]
aa=set(a) #converting to sets by typecasting
bb=set(b)
cc=set(c)
x=aa.intersection(bb) #taking only common values
y=bb.intersection(cc)
z=x.intersection(y)
print(list(z)) #printing the common values as list only by typecasting 

p=[1,5,5]
q=[3,4,5,5,10]
r=[5,5,20]
pp=set(p)
qq=set(q)
rr=set(r)
u=pp.intersection(qq)
v=qq.intersection(rr)
t=u.intersection(v)
print(list(t))
