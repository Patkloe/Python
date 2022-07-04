# method with complexity O(nlogn)
def mergesort(tab):
 if len(tab)>1:
  mid=len(tab)//2
  left=tab[:mid]
  right=tab[mid:]
  mergesort(left)
  mergesort(right)
  i=j=k=0
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
def indexfirstocc(l,x):  #pour avoir le premier index d'une occurence
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
  return -1
def lastindexocc(l,x): #pour avoir l'index de la derniere occurence
  low=0
  high=len(l)-1
  while low<=high:
   mid=(low+high)//2
   if l[mid]>x:
    high=mid-1
   elif l[mid]<x:
    low=mid+1
   else:
    if mid==mid-1 or l[mid]!=l[mid+1]:
     return mid
    else:
     low=mid+1
  return -1
def nbreocc(tab,i):
 if indexfirstocc(tab,i)>0:
  return (lastindexocc(tab,i)-indexfirstocc(tab,i))+1
 else:
  return -1

# method through diionary datastructure, complexity O(n)
def nbrebdict(tab,i):
 recup={}
 for j in tab:
  if j in recup:
   recup[j]+=1
  else:
   recup[j]=1
 if i in recup:
  return recup[i]
 else: 
  return -1
tab="yuopegtfvdvdfnbdmn"
print(mergesort(list(tab)))
newtab=mergesort(list(tab))
print(newtab)
print(indexfirstocc(newtab,"d"))
print(lastindexocc(newtab,"d")) 
print(nbreocc(newtab,"d"))
print(nbrebdict(newtab,"d"))
