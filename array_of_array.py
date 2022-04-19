thislist = [[1,2,3],[4,5,6],[3,7,9],[0,2,2],[0,1,7]]
for x in thislist:
 print(x)
print("organisation")
thislist.sort()
print(thislist)
print(thislist[0][2])
thislist.append("test")
print(thislist)
taille = len(thislist)
print(taille)
print(thislist[5])
print(thislist[5][2][0])
thislist.remove([0,1,7])
print(thislist)
le_type = type(thislist)
print(le_type) # pour recuperer le type de la variable thislist

