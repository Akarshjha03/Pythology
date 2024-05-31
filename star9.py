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