'''Write a program create 3x3 matrix using python. Take all the elements from the user. 
And also print the sum of diagonal elements from created matrix. '''



l=[]    #create an empty list for 3 lists inside

for i in range(0,3):  #create a loop to to append list 3 times

    k=[]   #an empty list for appending the list inside
    for j in range(0,3):
        k.append(int(input('enter integer: ')))
    
    l.append(k)

print(l)