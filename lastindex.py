def lastindex(l,x):
 low=0
 high=len(l)-1
 while low<=high:
  mid=(high+low)//2
  if l[mid]>x:
   high=mid-1
  elif l[mid]<x:
   low=mid+1
  else:
   #if mid==0 or l[mid-1]!=l[mid]:
   if mid==len(l)-1 or l[mid]!=l[mid+1]:
    return mid
   else:
    #high=mid-1
    low=mid+1
 return -1
tab=[10,10,10,20,20]
print(lastindex(tab,10))
