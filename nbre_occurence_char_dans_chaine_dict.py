test = ['a','b','c','a','d','c']
#nbre = test.count('a')
#char = str(test)
#print(nbre)
nouv = {}   # on initialise un dictionnaire qui va recuperer le nombre d'occurence d'un caractere dans la chaine
for j in test: # pour chaque charactere dans la chaine, le dictionnaire
 nouv[j] = test.count(j) # on compte le nombre d'apparitions dans la chaine on aura pour cle dans le dictionnaire le caharactere et pour valeur, le nombre d'occurence dans la chaine.
print(nouv)
