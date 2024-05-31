#pyramid pattern upward:
n=int(input("Enter the value of n:"))
for i in range(1,n+1):

    print(" " * (n-i),end="")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()