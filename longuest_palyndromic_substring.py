def partition(s): # function to write all substring contingent of a string, fonction pourecrire tout sous chaine d'une chaine
 deb=0
 temp=""
 res=[]
 while deb<len(s):
  temp+=s[deb]
  res.append(temp)
  i=deb+1
  for i in range(i,len(s)):
   temp+=s[i]
   res.append(temp)
   #i+=1
  temp=""
  deb+=1  #increment main loop
 return(res)
 
#s="abracadabra"
#print(partition(s))
def compare(s):  #determine si un charactere est palyndrome/ function to deetect palyndronic
 temp=""
 res=[]
 deb=0
 fin=len(s)-1
 while fin>=0:
  temp=temp+s[fin]
  fin-=1
 if temp==s:
   return True
 else:
  return False
 
#s="aba"
#print(compare(s))
def longsub(s):
 res=[]
 blt=partition(s)
 for x in blt:
  if compare(x):
   res.append(x)
 taille=0
 for y in res:
  val=len(y)
  if val>taille:
   taille=val
   affich=y
   print(affich)
   print(res)
 return taille
 
s="papa"
print(longsub(s))
