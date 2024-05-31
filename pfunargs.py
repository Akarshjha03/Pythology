#types of arguments in functions 
'''positional arguments:
jab bina variable ya variables ka value declare kiye arguments me pass kiye jaaye'''
def sum(n1,n2):
    val = n1+n2
    return val

ans = sum(3,5)
print(ans)

'''keyword arguments:
jab auguments me hi value ka parameters specify kare'''
gul = sum (n2=3,n1=9)
print(gul)

'''default arguments:
jab function ke parameter me hi hum default value set karo 
aur  agar hum function call pe kuch arguments naa pass kare
tho function default alue jo set hai ussi ko lega as arguments'''
def sub(p1=0,p2=0):
    diff = p1-p2
    return sub

my_val=sub(3)
print(my_val)
#here the value of p2 is specified  ,so  function will take 0 as p2 value as it is set  default


'''arbitary arguments (*args,**kwargs): #important but not that much in use 
when we dont know ki kitne parameters lagange(tho hum *args ka use karke 
kitne bhi arguments add kar sakte hai),the value added in args will be taken as tuple
eg. sum of n numbers'''
def summ(*args):
    summ = 0
    for i in args:#traversing through a tuple
        summ += i
        return summ
    
we = summ(1+2+3+4+5+6+7)
print(we)

'''(**kwargs):
this works the same way as *args and serves the same purpose
but,it value you enter in arguments it takes it as dictionary'''
def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentinfo(name="akarsh",age=20,city="mumbai")
studentinfo(name="nitish",age=25,city="palghar")
studentinfo(name="mehdi",age=21,city="ahmedabad")