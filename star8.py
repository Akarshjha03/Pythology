#python pyramid downward:
num=int(input("Enter the value of num:"))
for i in range(num,0,-1):
    print(" "*(num-i),end="")
    for j in range(1,2*i+1-1):
        print("*",end="")
    print()