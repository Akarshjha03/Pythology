#function to calculate factorial of a given number:
n = int(input("Enter the vlaue of n:"))

def facto(n):
    #following is also the code for factorial
    factorial=1
    if n<0:
        print("can't calculate factorial for negative nos.")
    elif n==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            factorial *= i
        print("the factorial of",n,"is",factorial)
    return factorial

#calling the function:
num = facto(n)