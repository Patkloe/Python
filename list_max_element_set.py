tab=[1,1,2,2,3,1,4,4,5,1,2,3,1,4,4,4,4]
max=0
nbre=0
const=set()
for i in tab:
 if i in const:
  nbre+=1
  if nbre>max:
   max=nbre
   index=i
 else:
  const.add(i)
 
 
print(i)
