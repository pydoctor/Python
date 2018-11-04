'''16.	Write a program find all even numbers from the given list.

Input_List = [18.8, “Hyd”, 18, 26.9, 19, “BANG”, 26, 33.7, 25, “CHEN”]
Output = [18, 26]
'''



'''
input_list = [18.8, 'Hyd', 18, 26.9, 19, 'BANG', 26, 33.7, 25, 'CHEN']
output=[]
for i in input_list:
    try:
        if i%2 == 0:
            output.append(i)
    except:
        TypeError
print(output)

'''
input_list = [18.8, 'Hyd', 18, 26.9, 19, 'BANG', 26, 33.7, 25, 'CHEN']
output = []


