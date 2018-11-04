'''11.	Write a program take 10 input strings of different lengths 
from the user and store all the strings into a list and 
display only odd length strings are the output in a list format.'''

''' mahee, indian, hindustan, germany,comedy,television,camera,google,microsoft,tesco

'''

l=[]
h=[]

for i in range (0,10):
    l.append(input('enter string: '))
    if len(l[i]) % 2 ==0:
        h.append(l[i])
print(l)
print(h)