def mergesort(arr):
 if len(arr)>1:
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  mergesort(left)
  mergesort(right)
  i=j=k=0
  while i<len(left) and j<len(right):
   if left[i]<right[j]:
    arr[k]=left[i]
    i+=1
   else:
    arr[k]=right[j]
    j+=1
   k+=1
  while i<len(left):
   arr[k]=left[i]
   i+=1
   k+=1
  while j<len(right):
   arr[k]=right[j]
   j+=1
   k+=1
  return arr
 else:
  return arr

def kthsmallest(arr,k):
 tab=mergesort(arr)
 return tab[k-1]
tab=[4,3,0,1,7,6,5,9,8]
k=5
print(kthsmallest(tab,k))
 
