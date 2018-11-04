'''7.	Write a program find the maximum number from the given input list
Input_list = [82, 62, 61, 54, 71, 89, 75, 73]
'''


Input_list = [82, 62, 61, 54, 71, 89, 75, 73, 1220]

max = Input_list[0]#initializing the first value to a variable and comparing them with rest.

for i in range(0, len(Input_list)):
    if max <= Input_list[i]:
        max = Input_list[i]

print ('The maximum number in given list is ', max)
        



