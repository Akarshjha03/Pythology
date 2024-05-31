#LIST
L=["abc",1,4,10.2]
print(type(L)) #for printing the data type of list 
print(len(L))  #for  printing the length of the list
print(L[-1])   #for printing the element at -1 location
               #sliceing index positions form right-left(..to-1) and left to right(0to...)

#SLICEING
B= "Hello i am AKARSH JHA"
print(B[::-1])    #printing the list in reverse 
print(B[0:-1:1])  #printing the string
print(B[-3:0:-1]) #analyse the printing

'''to insert a list item at a specified index, use the insert()'''
L.insert(6,"xyz") #yeh index ek value peeche kaam karta hai 
print(L)

'''to add the value in list use: list.append(element), Then print it
this will add the element at the last of the list'''
L.append(23)
print(L)

'''Add the elements of tropical to L'''
tropical = [89,'Bharat',57.67]
L.extend(tropical) #it adds elements to the last of the list 
print(L) 

#LIST CONCATE 
print(L+tropical) #somewhat similar to extend

'''replace value of string'''
# Replace Values in a List using indexing
l = [ 'Hardik','Rohit', 'Rahul', 'Virat', 'Pant']
        #0       1         2        3       4 
# replace first value
l[0] = 'Akarsh'

print(l)

#COUNT IN LIST:
a=[1,2,3,4,5]
a.count(1) #prints the list or elements of list
print(a)
a.remove(1) #to remove an element form the list
print(a)
a.pop(0) #remove the element from the list by index positions
print(a)
del a[0] #remove the element from the list by index positions
print(a)