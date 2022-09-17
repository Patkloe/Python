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
