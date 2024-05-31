'''A program that checks if a given string is a palindrome.'''


String = input(("Enter a letter:")) 
if String == String[::-1]: #or reversed(string)
 print("The letter is a palindrome") 
else: 
 print("The letter is not a palindrome")