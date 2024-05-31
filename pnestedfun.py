#nested function:
def outer_function():
    x=17

    def inner_function():
        y=6
        result = x+y
        return result
    
    return inner_function()

output=outer_function()
print(output)