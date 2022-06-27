def merge(l1,l2):
 i = 0
 j = 0
 size1 = len(l1)
 size2 = len(l2)
 res = []
 #while i<size1 & j<size2:
  #if l1[i] < l2[j]:
   #res.append(l1[i])
   #i = i + 1
  #else:
   #res.append(l2[j])
   #j = j+ 1
 while i < size1:
  res.append(l1[i])
  i = i + 1
 while j < size2:
  res.append(l2[j])
  j = j+ 1
 return res
 
tab1 = [2,3,5,6,7]
tab2 = [1,9,6,8,4,0]
print(merge(tab1,tab2))
# a bosser
#### Other version ######
def mergesort(tab):
 if len(tab)>1:
  mid=(len(tab))//2
  left=tab[:mid]
  right=tab[mid:]
  mergesort(left)
  mergesort(right)
  i=j=k=0 #left
  while i<len(left) and j<len(right):
   if left[i]<right[j]:
    tab[k]=left[i]
    i+=1
   else:
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

tab=[13,14,15,9,7,5,3,6,7,4,2,1,0]
print(mergesort(tab))


