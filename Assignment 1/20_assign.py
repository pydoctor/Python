'''20.	Write a program reverse each string from the given list 
and finally reverse a list'''





l=['kakarla','mahee', 'rohit', 'india']
for i in range(0, len(l)):
    ele = l[i]
    l[i]= (ele[-1::-1])

print(l[-1::-1])