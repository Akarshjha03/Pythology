#1st type pattern:

n=int(input("Enter the value of n:"))
for i in range(n):
    print("*" * n)
    
m=int(input("Enter the value of m:"))
for i in range(m):
    print(123456)
    
#2nd type pattern:
     
p=int(input("Enter the value of p:"))
for i in range(1,p+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
q=int(input("Enter the value of q:"))
for i in range(1,q+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
    
r=int(input("Enter the value of r:"))
for i in range(1,r+1):
    for j in range(r-1):
        print("",end="")
    for k in range(1,i+1):
        print(chr(64+k),end="")
    print()

#3rd type pattern:
#diamond pattern:
n=int(input("Enter the value of n:"))
#first upper half
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()

#second lower half:
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()