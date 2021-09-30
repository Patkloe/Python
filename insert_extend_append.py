fruits = ['apple', 'banana', 'cherry']
cars = ['VW','Volvo', 'Toyoya']
deb = len(fruits)
fruits.insert(len(fruits), "orange") # insert an element in a specific position in the list
fin = len(fruits)
print(fruits)
print(deb)
print(fin)
fruits.extend(cars) # add elements of a list in another list
print(fruits)
fruits.append("Decouvrir") # add an element at the end of the list
print(fruits)
