def countval(arr,s):
 deb=0
 fin=len(arr)
 sum=0
 res=[]
 while deb<fin:
  sum=sum+arr[deb]
  res.append(deb)
  if sum<s:
   deb+=1
  elif sum>s:
   res=[]
   sum=0
   deb=deb-1
  else:
   return res
 return 0
 
arr=[1,2,3,5]
s=5
print(countval(arr,s))
   
