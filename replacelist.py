'''Given a list in Python and provided the index of the elements,
write a program to swap the two elements in the list.
EXAMPLES:
Input : List = [23,65,19,80], idx1 = 0, idx2 = 2
Output : [19, 65, 23,90]
Input : List = [1,2,3,4,5], idx1 = 1, idx2 = 4
output: [1,5,3,4,2]'''

list1=[23,65,19,80]
list1[0]=19
list1[2]=23
print(list1)

list2=[1,2,3,4,5]
list2[1]=5
list2[4]=2
print(list2)

#it can be done in other ways also like one in the video but those are lonng and complex
#and rather it doeesnt uses any new/diferent functions to print the out but different ways
#like input loop & if and mine is using change value of list using index