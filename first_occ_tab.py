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
# there the function
def rechfirst(tab,i):
 if len(tab)>1:
  low=0
  high=len(tab)-1
  while low<=high:
   mid=(low+high)//2
   if tab[mid]<i:
    low=mid+1
   elif tab[mid]>i:
    high=mid-1
   else:
    high=mid-1
    return mid
    '''if mid==0 or tab[mid]!=tab[mid-1]:
     return mid      other idea
    else:
     high=mid-1'''
  return -1
tab="yuopegtfvdvdfnbdmn"
print(mergesort(list(tab)))
newtab=mergesort(list(tab))
print(newtab)
print(rechfirst(newtab,"b"))
