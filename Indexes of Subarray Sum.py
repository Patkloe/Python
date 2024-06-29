def searchsum(arr,sum):
 temp=""
 res=[]
 for i in range(len(arr)):
  temp=temp+str(arr[i])
  print(temp)
  if len(temp)==2:
   if int(temp[0])+int(temp[1])==sum:
    res.append(arr.index(int(temp[0])))
    res.append(arr.index(int(temp[1])))
    temp=temp[1]
   else:
    temp=temp[1]
 return res
 
 
arr=[4,1,3,4,5]
print(searchsum(arr,5))
