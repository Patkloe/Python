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

# other version

def bSearch(l, x):
    low = 0
    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


l = [10, 20, 30, 40, 50, 60]

print(30, bSearch(l, 30))
print(20, bSearch(l, 20))
print(10, bSearch(l, 10))
print(60, bSearch(l, 60))
print(40, bSearch(l, 40))
print(55, bSearch(l, 55))
print(-50, bSearch(l, -50))

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
  
  
tab=[0,1,2,3,4,5,6,7,8,9]
print(binarysearch(tab,-2))
  


  
