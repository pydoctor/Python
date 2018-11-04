'''12.	Write a program find all even number from
 the given input list and display output as a list format. 
 '''

input_list = [1,2,3,4,5,6,7,8,9,10]
output=[]

for i in input_list:
    if i % 2 == 0:
        output.append(i)

print(output)
