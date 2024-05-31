#creating a set:
name={"Akarsh","Nitish","Mehdi","Bhatia"}
print(name) #printing a set

print(len(name)) #checking the length of set
print(type(name)) #checking the type of set

#accesing items of set:(as here there is no indexing so we will use for loop to access items)
for i in name:
    print(i)

#to check if item exist inside set or not:(using membership operator)
if "Akarsh" in name:
    print("Akarsh is in name")

#to add a item inside a set
name.add("Nikhil.k")
print(name)

#to remove a item from set
name.remove("Bhatia")
print(name)
'''OR'''
#name.discard("Bhatia")'''this fn throws no error when if item is not in set
#print(name)

#to add other datatype inside set
phone={"mac","intel","amd"}
name.update(phone)
print(name)

#joining 2 sets
s1={"a","b","c"} 
s2={"d","e","a"}
s3=s1.union(s2) #no duplicate values allowed
print(s3)

#keep only duplicates while joining
s4=s1.intersection(s2)
print(s4)

#keep all values except same
s1.symmetric_difference_update(s2)
print(s1)