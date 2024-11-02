tab=[1,1,2,3,4,4,4,7,7,6,6,6]
def minsdj(tab):
 ret=dict()
 for i in range(len(tab)):
  ret[tab[i]]=tab[i]
 return list(ret.keys())
print(minsdj(tab))
