x = 1
comp = isinstance(x,complex) # pour checker le type d'une variable, python on utilise la fonction isintance(x,y) x = variable a checker, y class/object 'complex','int', 'float','str'
if comp == True:
 print(type(x))
else:
 print("Mauvais type")
