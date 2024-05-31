#function to check if a string is palindrome or not:

sup=input("Enter the value of string:")
def panli(s):
    if sup == sup[::-1]:
        print("The given string is Palindrome")
    else:
        print("The given string is not a palindrome")

panli(sup)