def rech(arr,x):
 deb=0
 fin=len(arr)-1
 while deb<=fin:
  mid=(deb+fin)//2
  #print(mid)
  if arr[mid]==x:
   return mid
  elif arr[mid]>x:
   fin-=1
  else:
   deb+=1
 return -1
 
 
tab=["a","b","c","d","e","f","g","h"]
print(rech(tab,"f"))
