def firstindex(l,x):
 low=0
 high=len(l)-1
 while low<=high:
  mid=(high+low)//2
  if l[mid]>x:
   high=mid-1
  elif l[mid]<x:
   low=mid+1
  else:
   if mid==0 or l[mid-1]!=l[mid]:
    return mid
   else:
    high=mid-1
 return -1
tab=[5,10,10,20,20]
print(firstindex(tab,10))
