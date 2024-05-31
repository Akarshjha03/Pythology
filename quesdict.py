'''given a dictionary {"a":100,"b":200,"c":300}
add the values of keys and the answer should be 600 as output'''

val = {
    "a":100,
    "b":200,
    "c":300
}
sum = val["a"] + val["b"] + val["c"] #our own developed way
print(sum)
#other way:
#print(sum(val.values()))

'''given a dictionary {"x":25,"y":18,"z":45}
add the values of keys and the answer should be 88 as output'''

val1 = {
    "x":25,
    "y":18,
    "z":45
}
sum1 = val1["x"] + val1["y"] + val1["z"]
print(sum1)
