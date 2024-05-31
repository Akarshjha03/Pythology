#step pattern 1st part:
num=int(input("Enter the value of num:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#step pattern second part
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()