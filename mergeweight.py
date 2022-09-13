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
  
# other version
def compare(a,b):
 if a<b:
  return True
 else:
  return False

def Evalue(tab):
 res=[]
 val=0
 i=0
 '''while i<n:
  j=i+1
  if j<len(tab) and compare(tab[i],tab[j]):
   #nbre+=1
   val=tab[i]+tab[i+1]
   tab.remove(tab[i+1])
   tab[i]=val
   #i=0
   print(tab)
   print(len(tab))
   Evalue(tab,len(tab))
  #elif j<len(tab) and not compare(tab[i],tab[i+1]):
  i+=1'''
 for i in range(len(tab)):
   j=i+1
   if j<len(tab) and compare(tab[i],tab[j]):
    val=tab[i]+tab[i+1]
    tab.remove(tab[i+1])
    tab[i]=val
    print(tab)
    Evalue(tab)
 return max(tab)
 
tab=[4,2,9,10,3,7]
print(Evalue(tab))

#good version
def compare(x,y):
 if x<y:
  return True
 else:
  return False
  
def mergeweight(tab):
 val=0
 '''i=0
 while i<len(tab):
  j=i+1
  if j<len(tab) and compare(tab[i],tab[j]):
   val=tab[i]+tab[j]
   tab.pop(tab[j])
   tab[i]=val
   print(tab)
   mergeweight(tab)
  elif j<len(tab) and not compare(tab[i],tab[j]):
   i+=1
  i+=1'''
 for i in range(len(tab)):
   j=i+1
   if j<len(tab) and compare(tab[i],tab[i+1]):
    val=tab[i]+tab[i+1]
    tab.pop(i+1)
    tab[i]=val
    print(len(tab))
    print(tab)
    mergeweight(tab)
 return tab
tab=[8,9,1,4,3,5,7,8,2,3,4]
print(mergeweight(tab))
  
