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
# version to get the element  with amount higher than the size of array divide by 2

tab=[1,1,2,2,1]
max=len(tab)/2
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
#  another test
tab=[1,1,2,2,1,2,2,2,2,3,3,4,2,2,2]
max=len(tab)/2
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
