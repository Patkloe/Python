tab=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
ret=[]
for i in tab:
 ret.append(i[1])
rev=sorted(ret)
res=[]
for i in rev:
 for j in tab:
  if i==j[1]:
   res.append(j)
print(res)
