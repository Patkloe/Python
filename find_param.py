print("Hello, World!")

test = "pourterenverser"
unp=[*test]
rev=unp[::-1]
res="".join(rev)
print(res)
voir="testisagoodthing"
ins="tisag"
a = ins  not in voir
print(a)
print(ins.rfind("a")) #find does not raise an error
#print(ins.index("b")) # raise an error

testpat="venez me retrouvez"
ch = "ez"
print(testpat.find(ch)) # cherche sur toute la chaine de charactere et retourne la position du premier index trouve
print(testpat.find(ch,5,17))# cherche texte ds la variable pointe par la variable ch, commencant a la position 5, finissant a la position 17 exclusif
print(testpat.find(ch,5)) #cherche a la position commencant a 'index 5, jusqu'a la fin de la chaine
print(testpat.find(ch,5,18))
