'''Given a string and a number N, we need to mirror the characters
from the N-th position up to the length of the string in
alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to
'y', and so on.

Input : N = 3(paradox)
Output : paizwlc

Input : N = 6 (pneumonia)
Output : pneumlmrz'''

str1 = list("paradox")
print(type(str1))
str1[2]="i"
str1[3]="z"
str1[4]="w"
str1[5]="l"
str1[6]="c"
print(str(str1[0]+str1[1]+str1[2]+str1[3]+str1[4]+str1[5]+str1[6]))

str2=list("pneumonia")
str2[5]="l"
str2[6]="m"
str2[7]="r"
str2[8]="z"
print(str(str2[0]+str2[1]+str2[2]+str2[3]+str2[4]+str2[5]+str2[6]+str2[7]+str2[8]))

