'''19.	Write a program convert the following list to a dictionary. 
X = [(“A”, 65), (“B”, 66), (“C”, 67), (“D”, 68)]
'''


X = [('A', 65), ('B', 66), ('C', 67), ('D', 68)]

#print(dict(X))

dct = {}

for i in range(0,len(X)):
    dct[X[i][0]] = X[i][1]

print(dct)