def cherche(arr,val):
 deb=0
 fin=len(arr)-1
 while deb<=fin:
  if arr[deb]!=val and arr[fin]!=val:
   deb+=1
   fin-=1
  elif arr[deb]!=val:
   return fin
  elif arr[fin]!=val:
   return deb
  else:
   return deb,fin
 return -1
   
print(cherche([3,4,5,6,2,8,0,3],3))
