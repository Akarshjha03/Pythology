#function to reverse a string 
#(var_name.reverse())is used in list for reversing in string we need to use sliceing
#sim = "akarsh"
#print(sim[::-1])

stringss = input("Enter a string:")
def revst(*args):
    stringss_rev= print(stringss[::-1])
    return stringss_rev

rev_str= revst()