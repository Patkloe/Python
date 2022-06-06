def verif_dict(tab):
 sol={}
 for i in tab:
  if i in sol:
   sol[i]+=1
  else:
   sol[i]=1
 return sol
tab=[1,1,1,3,4,5,5,8,8,7,7]
print(verif_dict(tab))


# different version
def verif_dict(tab):
 sol={}
 for i in tab:
  if i in sol:
   sol[i]+=1
  else:
   sol[i]=1
 #for i in sol:
  if sol[i]>(len(tab)/2):
   print(i)
 return sol
tab=[1,1,1,3,4,5,5,8,8,7,7]
print(verif_dict(tab))
#to check tonight
def verif_dict(tab):
 sol={}
 for i in tab:
  if i in sol:
   sol[i]+=1
  else:
   sol[i]=1
 # here condition to display the result
 return sol
tab=[1,1,1,3,4,5,5,8,8,7,7]
print(verif_dict(tab))
