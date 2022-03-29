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
