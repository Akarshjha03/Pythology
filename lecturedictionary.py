#dictionary:collection of key-value pairs
d={"fruit":["apple","guava"],"Akarsh":"iphone","amba":"oppo"}
print(d["Akarsh"])
print(type(d))
#it is ordered
#it works like dictionary
print(len(d))

#change value of key inside dictionary:
d["amba"]="redmi"
print(d["amba"])
#key should be unique,value can be same
print(d)#print whole dictionary

#get method to  access value of dictionary
v=d.get("fruit")
print(v)
print(type(v))
d.get("Akarsh")

#delete key and value both from dictionary
del d["Akarsh"]
print(d)

#delete the element from the list
d.pop("fruit")
print(d)

#add element form end using append
d["akarsh"]="iphone"
print(d)

#join two dictionary
d2={"watch":"titan","shoes":"puma"}
d["name"]=d2
print(d)