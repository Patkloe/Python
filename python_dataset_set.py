thisset = {"apple", "banana", "cherry","banana"} # definition de notre dataset set
print(thisset)
for x in thisset : # pour parcourir les elements du set
 print(x)  # imprime ces elements
test = {1,2,3,4,5,1,2,3} # les elements d'un set sont uniques, ici on fait le test
for y in test :       # on parcourt les elements du set et il affichera 1, 2, 3, 4, 5
 print(y)   # impression des elements du set
tab = [1,2,3,4,5,1,2,3]   # script pour attribuer dynamiquement des elements a une variable set,  ici on defini le tableau
setel = {'a'}     # on initialise le set qui va garder les elements donnes par le tableau
nbre = len(tab)
for i in range(0,nbre) :
 setel.add(tab[i])  # on utilise la methode add, pour ajouter des elements dans le set
for j in setel :
 print(j)
# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.
