#creating a function to take average of list elements
#as there is no predefined fn to take avg of list elements(so we have to create it)

'''taking a list elements input from user'''
lst=[] #creating an empty list
n=int(input("Enter the elements:")) #no. of elements in list

for i in range(0,n): #printing all the elements entered
    ele=(int(input()))  #a variable to store input
    lst.append(ele)   #adding the elements to the list

#print the list
print(lst)

'''actual function'''
def avg(*args):
    avgg = (sum(lst))/len(lst)
    return avgg

#calling the function:
org_avg= avg(lst)
print(org_avg)