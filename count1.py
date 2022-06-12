def mergesort(tab):
 if len(tab)>1:
  mid=len(tab)//2
  left=tab[:mid]
  right=tab[mid:]
  mergesort(left)
  mergesort(right)
  i=0 #left
  j=0 #right
  k=0 #tab
  while i<len(left) and j<len(right):
   if left[i]<right[j]:
    tab[k]=left[i]
    i=i+1
   else:
    tab[k]=right[j]
    j=j+1
   k=k+1
  while i<len(left):
   tab[k]=left[i]
   i=i+1
   k=k+1
  while j<len(right):
   tab[k]=right[j]
   j=j+1
   k=k+1
  return tab
 else:
  return tab
def firstocc(tab,x):
 low=0
 high=len(tab)-1
 while low<=high:
  mid=(low+high)//2
  if tab[mid]>x:
   high=mid-1
  elif tab[mid]<x:
   low=mid+1
  else:
   if mid==0 or tab[mid]!=tab[mid-1]:
    return mid
   else:
    high=mid-1
def indexfirstocc(l,x):  #pour avoir le premier index d'une occurence
 if x in l:
  low=0
  high=len(l)-1
  while low<=high:
   mid=(low+high)//2
   if l[mid]>x:
    high=mid-1
   elif l[mid]<x:
    low=mid+1
   else:
    if mid==0 or l[mid]!=l[mid-1]:
     return mid
    else:
     high=mid-1
 else:
   return -1
def indexlastocc(l,x):  #pour avoir le premier index d'une occurence
 if x in l:
  low=0
  high=len(l)-1
  while low<=high:
   mid=(low+high)//2
   if l[mid]>x:
    high=mid-1
   elif l[mid]<x:
    low=mid+1
   else:
    if mid==len(l)-1 or l[mid]!=l[mid+1]:
     return mid
    else:
     low=mid+1
 else:
   return -1
def nbreocc(tab,x):
 if firstocc(tab,x)>=0:
  return indexlastocc(tab,x) - indexfirstocc(tab,x) + 1
 else:
  return -1
tab=[1,1,1,1,0,0,0]
print(mergesort(tab))
res=mergesort(tab)
print(firstocc(res,1))
print(indexfirstocc(res,1))
print(indexlastocc(res,1))
print(nbreocc(res,1))
