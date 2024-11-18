tab=[1,2,3,4,5,7,8,9]
temp=tuple()
res=[]
for i in tab:
 temp+=(i,)
 if len(temp)==2:
  res.append(temp)
  temp=()
print(res)
tp=(1,2)
print(len(tp))
 tab=["tre","yui","opi","cdf","rty","mkl","klo"]
res=[]
temp=[]
for i in range(len(tab)):
 for j in range(i+1,len(tab)):
  temp.append(tab[i])
  temp.append(tab[j])
  if len(temp)==2:
   nouv=tuple(temp)
   res.append(nouv)
   temp=[]
print(res)
tab=["tre","yui","opi","cdf","rty","mkl","klo"]
res=[]
temp=[]
for i in range(len(tab)):
 for j in range(i+1,len(tab)):
  temp.append(tab[i])
  temp.append(tab[j])
  if len(temp)==2:
   nouv=tuple(temp)
   res.append(nouv)
   temp=[]
print(res)
tup=()
test=[]
for i in range(len(tab)):
  tup+=(tab[i],)
  print(tup)
  if len(tup)==2:
   test.append(tup)
   tup=()
print(test) 


