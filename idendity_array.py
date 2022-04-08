def idendity_array(tab):
 deb=0
 fin=len(tab)-1
 while deb<=fin:
  if tab[deb]==tab[fin]:
   print(tab[deb]) 
   print(tab[fin])
   deb+=1
   fin-=1
  else:
   return -1
tab=["a","a","a","a","a","c","a","a","a","a"]
print(idendity_array(tab))
