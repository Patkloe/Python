def invertcount(tab):
 if len(tab)>1:
  mid=len(tab)//2
  left=tab[:mid]
  right=tab[mid:]
  invertcount(left)
  invertcount(right)
  i=j=k=nbre=0
  while i<len(left) and j<len(right):
   if left[i]<right[j]:
    tab[k]=left[i]
    i+=1
   else:
    nbre+=1
    print(nbre)
    tab[k]=right[j]
    j+=1
   k+=1
  while i<len(left):
   tab[k]=left[i]
   i+=1
   k+=1
  while j<len(right):
   tab[k]=right[j]
   j+=1
   k+=1
  return tab
 else:
  return tab
tab=[3,2,1,0]
print(invertcount(tab))
