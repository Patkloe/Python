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
 
