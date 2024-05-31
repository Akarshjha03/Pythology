#function to chheck if a function is prime or not:
n=int(input("Enter the value of n:"))

def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

prime(n)