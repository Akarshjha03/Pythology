#creating a function for sum of 1 to n:
n=int(input("Enter the value of n:"))
def sum1ton(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
#calling the function: 
output=sum1ton(n)
print(output)

#calling the function again(one more time),code resuability:
n1=int(input("Enter the value of n1:"))
output1=sum1ton(n1)
print(output1)