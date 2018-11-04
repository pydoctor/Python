'''Write a program join each and every character from the given string with hyphen(-)
Example: 
Input_str = “PYTHON”
Output = P-Y-T-H-O-N
Note: Please Don’t use join () function.   '''

input_str = 'PYTHONPROGRAMMING'
output = input_str[0]

for i in range(1, len(input_str)):
    output = output+'-'+input_str[i]

print(output)
    