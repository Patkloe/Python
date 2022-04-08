def parcourt_array(tab):
 deb=0
 fin=len(tab)-1
 while deb<=fin:
  print(tab[deb]) 
  print(tab[fin])
  deb+=1
  fin-=1
 return deb,fin
tab=["a","b","c","d","e","f","g","h","i","j"]
print(parcourt_array(tab))



'''print(parcourt_array(tab))
i = 1
j = 6
while i <= j:
  print(i)
  print(j)
  i += 1
  j -= 1'''
