def rech(arr,x):
 deb=0
 fin=len(arr)-1
 while deb<=fin:
  mid=(deb+fin)//2
  #print(mid)
  if arr[mid]==x:
   return mid
  elif arr[mid]>x:   # always the condition
   fin=mid-1
  else:  # reverse of all other conditions
   deb=mid+1
 return -1
 
 
tab=["a","b","c","d","e","f","g","h"]
print(rech(tab,"f"))

#given a sorted list, search a specific element in that array
def binarysearch(l,x):
 deb=0
 fin=len(l)-1
 while deb<=fin:
  mid=(deb+fin)//2
  if l[mid]>x:
   mid-=1
  elif l[mid]<x:
   mid+=1
  else:
   return mid
 return -1
 
tab=[1,2,3,4,5,6,7]
x=4
print(binarysearch(tab,x))
  
