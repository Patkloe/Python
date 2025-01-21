tab=[0,0,0]
target=1
i=0
res=[]
temp=[]
val=0
while i<len(tab):
 j=i+1
 while j<len(tab):
  k=j+1
  while k<len(tab):
   temp.append(tab[i])
   temp.append(tab[j])
   temp.append(tab[k])
   if len(temp)==3:
    print(temp)
    mnt=sum(temp)
    print(mnt)
    sub=target-mnt
    if sub>=0:
     res.append(sub)
   temp=[]
   k+=1
  j+=1
 i+=1
print(min(res))
