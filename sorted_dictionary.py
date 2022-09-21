glo={}
recup=[]
tab=["1 3 4","2 3 4","5 4 7"]
for i in tab:
 exp=i.split(" ")
 for j in range(len(exp)-1):
  recup.append(exp[j])
for k in recup :
 if k in glo:
  glo[k]+=1
 else:
  glo[k]=1
sort_orders = sorted(glo.items(), key=lambda x: x[1], reverse=True)
print(sort_orders)

tab=[7,5,6,8,4,5]
rev=sorted(tab,reverse=True)
print(rev)

# under a function
def feedback(logs):
 recup=[]
 res={}
 for i in logs:
  recup.append(i)
 for x in recup:
  temp=x.split(" ")
  print(temp)
  for i in range(len(temp)-1):
   if temp[i] in res:
    res[temp[i]]+=1
   else: 
    res[temp[i]]=1
  final=sorted(res.items(),key=lambda a:a[i],reverse=True)
 return final

logs=["5 3 2","9 7 5","7 8 5","6 5 7","2 4 3","8 6 5","7 6 5","2 3 7","6 5 8","4 5 9"]
print(feedback(logs))
 
