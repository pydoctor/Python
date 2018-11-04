'''13.	Given a string of even length and print the output as 
string contains last half added with first half of the given string'''

input_string = 'abcdefghij'
i = len(input_string)//2
if len(input_string)%2 == 0:
    print(input_string[i:] + input_string[0:i])
