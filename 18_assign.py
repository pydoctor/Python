'''18.	Write a program create a random list of length 10 and 
print all the elements except the elements which are divisible by 4. '''

import random

org_list=[]
div_four=[]

for i in range(0,10):
    k=random.randrange(1,100)
    org_list.append(k)
    if k%4 ==0:
        div_four.append(k)


print(org_list)
print(div_four)