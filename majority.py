def majority():
 tab=[1,1,1,2,3,4,5,2,2,2,3,5,2,1,1,1]
 dic={}
 maj=0
 for i in range(len(tab)):
  dic[tab[i]]=tab.count(tab[i])
  if dic[tab[i]]>maj:
   maj=dic[tab[i]]
   ind=i
 print(dic)
 return maj,i    # return a tuple
 
print(majority())

# different version
def recherche_maxapp(tab,N):
 max=0
 maj=N/2
 sol={}
 ind=-1
 for i in tab:
  if i in sol:
   sol[i]+=1
  else:
   sol[i]=1
 for j in sol:
  if sol[j]>max:
   ind=j
   max=sol[j]
 if max>maj:
  return ind
 else:
  return -1
 
tab=[2,3,4,7,8,2,2,2,2]
print(recherche_maxapp(tab,9))
