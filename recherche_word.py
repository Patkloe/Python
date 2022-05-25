def decouv():
 test="je veux voir la manifestation de la recuperation des mots que l'on peut faire dans une longue phrase"
 cherch="recuperation"
 tab=[]
 tab=test.split(" ")
 print(tab)
 i=0
 while i<len(tab):
  if tab[i]==cherch:
   return i
  print(tab[i])
  i+=1
  '''if tab[i]==cherch:
   break
   return i
  else:
   return -1'''
 #return tab

print(decouv())
