#FOR LOOP IN PYTHON:
a=[1,2,3,4]
for x in a: #traversing:to process every character in a string, usually from left end to right end
    print(x)
if 3 in a: #printing specific element in from list ,if it exist 
    print("Yes")

#print index no. of list 
for x in range(4):
    print(x)

#for syntax:
'''for  condition
    print'''

#print elements of list by using index
s=[1,2,3,4]
for i in range(len(s)):
    print (s[i])

#for loop in single printing statement
[print (x) for x in s]

#WHILE LOOP IN PYTHON:
i = 0
while i < 5:
  print(i)
  i += 1

#for loop  in python is only used for traversing 
#while loop in python is used as normal loop  ie. for  printing number 0 to 100 for example
  
#adding all elements of list using function
b=[1,2,3,4]
sum_of_elements = sum(b)
print("Sum of elements in a list: ",sum_of_elements)

#adding all elements of list using while loop
s=[1,2,3,4,5]
i=0
total=0
while i< len(s):
    total= total+s[i]
    print(total)
#adding all elements of list using for loop
s[1,2,3,4,5]
sum=0

for i in range[len(s)]:
    sum = sum + s[i]
print (sum)
# THERE IS NO DOWHILE LOOP IN PYTHON
