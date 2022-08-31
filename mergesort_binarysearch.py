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

def binarysearch(tab,n):
 if len(tab)>1:
  left=0
  right=len(tab)-1
  while left<=right:
   mid=(left+right)//2
   if tab[mid]<n:
    left=mid+1
   elif tab[mid]>n:
    right=mid-1
   else:
    return mid 
  return -1
 else:
  return -1
    
mat=[9,5,7,3,4,0,1,2,6,8]
tab=mergesort(mat)
print(binarysearch(tab,9))
  
 
