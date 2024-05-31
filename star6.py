num=int(input("Enter the value of n:"))
for i in range(1,num+1):
    for j in range(num-1):
        print("",end="")
        for k in range(1,i+1):
            print(chr(64+k),end="")
        print()