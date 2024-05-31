'''A program that generates a multiplication table for a given number.'''


number=int(input("Enter the number:\n"))
for i in range(1, 11):
 print(number, 'x', i, '=', number*i)