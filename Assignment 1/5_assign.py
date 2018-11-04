'''5.	Write a program replace each string with an integer value
 in a given list of strings. The replacement integer value 
 should be sum of ascci values of each character of the same string. 
holy_rivers =["Ganges", "Godavari", "Brahmaputra", "Narmada", 
              "Yamuna", "Mahanadi", "Kaveri”, “Tapti"]
Hint: To get the ascii value of a charcter we need to use ord() function
Ex: ord("A") returns an integer value i.e 65- ascci value of A
'''

holy_rivers =["Ganges", "Godavari", "Brahmaputra", "Narmada", 
                "Yamuna", "Mahanadi", "Kaveri", "Tapti"]

for i in range(0, len(holy_rivers)):
    sum=0
    for j in holy_rivers[i]:
        sum = sum + ord(j)
    holy_rivers[i] = sum
    
print(holy_rivers)
    