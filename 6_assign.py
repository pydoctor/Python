'''6.	WAP print all duplicated values in descending order from the given input list. 
Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
Output: 
Duplicated elements: [403, 401]
'''


Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
Duplicate_list=[]
Duplicate_elements=[]


for i in Input_list:
    if Input_list.count(i)>1:
        Duplicate_list.append(i)

for ele in Duplicate_list:
    if ele not in Duplicate_elements:
        Duplicate_elements.append(ele)

print(sorted(Duplicate_elements,reverse=True))
