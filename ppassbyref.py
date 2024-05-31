#pass by refrence (functions):
def modifylist(lst):
    lst.append(4)
    #lst=[4,5,6,7]
    print("inside fn:",lst)

lst=[1,2,3]
modifylist(lst)
print("outside fn:",lst)