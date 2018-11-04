'''8.	Write a program change the given input list by  doing rotate left.
Ex: input [4, 5, 6, 7] output [5, 6, 7, 4]
'''

'''
l = [4,5,6,7]

l[0],l[1],l[2],l[3] =  l[1],l[2],l[3],l[0]

print(l)
'''


l=[4,5,6,7]
num=l[0]

for i in range (0,len(l)-1):
        l[i]=l[i+1]
l[len(l)-1]=num

print(l)