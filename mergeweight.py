def compare(x,y):
 if x<y:
  return True
 else:
  return False
def mergeweight(tab,s):
 val=0
 i=0
 print(tab)
 #while i<len(tab):
 for i in range(s):
  j=i+1
  if (j<len(tab) and compare(tab[i],tab[j])):
   val=tab[i]+tab[j]
   tab.remove(tab[j])
   tab[i]=val
   print(tab)
   m=len(tab)
   mergeweight(tab,len(tab))
  #i+=1
 return tab
 
tab=[5,6,9,8,7,1,2,3,4]
print(mergeweight(tab,9))
   
