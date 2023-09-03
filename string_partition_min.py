def partition_min():
 c="test_propable"
 val=[]
 i=0
 var=""
 while i<len(c):
  if c[i] not in var:
   var=var+c[i]
   print(var)
   i+=1
  else:
   print(var)
   val.append(var)
   var=""
   k=i
   i=k
 val.append(var)
 return len(val)
print(partition_min())
   
