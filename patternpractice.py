n=int(input("Enter the value of n:"))
#static pattern
for i in range(n):
    print("*" * n) 

for i in range(n):
    print("123456")

#dynamic pattrn
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i  in range(1,n+1):
    for j in range(n-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(64 + k),end="")
    print()

#diamond pattern:
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print("*",end="")
    print()

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()

