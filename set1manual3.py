'''A program that generates a random password of a specified length.'''

import random
import string
n = int(input("Enter the value of n:"))
def strong_level_pass(n):
 # Random character generation
 print("Strong level password: ", end="")
 for i in range(n):
 # Random special characters or digits
    print(random.choice(string.ascii_letters + string.digits + string.punctuation), end="")
 print()
 
if __name__ == '__main__':
 num = n
 strong_level_pass(num)