'''1.	WAP find the average of given list of elements 
representing a grade of student.
grades = [84, 84, 93, 78, 86, 73]
Note: Please don’t use sum() function to add the
 elements from a list
'''

grades = [84, 84, 93, 78, 86, 73]
'''print(sum(grades))'''# will give the sum of all the elements in the list.
sum=0
for ele in grades:
    sum = sum + ele
print ('The average of the grades is : ',(sum)/len(grades))
# Divison returns a float value.


#print(sum(grades)/len(grades)) will return the same result,
#however check if you defined a variable with function name
#cause that result to Type error(Int value cannot be callable)