#pass by value (functions):
def add_one(x):
    x = x + 1 #or x += 1
    print("value inside the function:",x)

x=5
add_one(x)
print("value outside the function:",x)