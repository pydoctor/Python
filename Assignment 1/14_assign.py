'''14.	WAP replace each string from the given list 
with the same string which is repeated with length of the string '''

Input = ['a', 'aa', 'abc', 'mahee']

for i in range(0, len(Input)):
    Input[i] = (Input[i] * len(Input[i]))

print(Input)