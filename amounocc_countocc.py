def mergesort(l):
 if len(l)>1:
  mid=len(l)//2
  left=l[:mid]
  right=l[mid:]
  mergesort(left)
  mergesort(right)
  i=j=k=0
  while i < len(left) and j < len(right):
   if left[i]<right[j]:
    l[k]=left[i]
    i+=1
   else:
    l[k]=right[j]
    j+=1
   k+=1
  while i<len(left):
    l[k]=left[i]
    i+=1
    k+=1
  while j<len(right):
   l[k]=right[j]
   j+=1
   k+=1
  return l
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
def lastindexocc(l,x): #pour avoir l'index de la derniere occurence
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
    if mid==mid-1 or l[mid]!=l[mid+1]:
     return mid
    else:
     low=mid+1
 else:
   return -1
def amountofocc(l,x):
 if indexfirstocc(l,x)>=0:
  return lastindexocc(l,x)-indexfirstocc(l,x)+1
 else:
  return 0
tab=[5,0,0,3,6,7,9,8,1,1,5,7,7,5]
tabs=mergesort(tab)
print(tabs)
print(indexfirstocc(tabs,5))
print(lastindexocc(tabs,5))
print(amountofocc(tabs,5))
print(indexfirstocc(tabs,4))
print(lastindexocc(tabs,4))
print(amountofocc(tabs,4))

# different version

def firstocc(tab,x):
 deb=0
 fin=len(tab)-1
 while deb<=fin:
  mid=(deb+fin)//2
  if tab[mid]<x:
   deb=mid+1
  elif tab[mid]>x:
   fin=mid-1
  else:
   if mid==0 or tab[mid]!=tab[mid-1]:
    return mid
   else:
    fin=mid-1

tab=[1,2,2,2,3,4,4,4,5,6,7,8,9]
x=4
print(firstocc(tab,x))
def lastocc(tab,x):
 deb=0
 fin=len(tab)-1
 while deb<=fin:
  mid=(deb+fin)//2
  if tab[mid]<x:
   deb=mid+1
  elif tab[mid]>x:
   fin=mid-1
  else:
   if mid==mid-1 or tab[mid]!=tab[mid+1]:
    return mid
   else:
    deb=mid+1
tab=[1,2,2,2,3,4,4,4,5,6,7,8,9]
x=4
print(lastocc(tab,x))

#Version with PYTHON predefined functions
def nbreocc(tab,x):
 #val="".join(tab)
 return(tab.rfind(x) - tab.find(x))
tab="VEUT DECOUVRIR"
x="R"
print(nbreocc(tab,x))
