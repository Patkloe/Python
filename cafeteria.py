def verif(tab,nouv,k):
 fin=True
 for j in tab :
  cal=j-nouv
  if abs(cal)<k:
   fin=False
   break
 return fin
def indice(tab,k,occup):
 nbre=0
 val=True
 for i in tab:
  if i not in occup:
   a=i-k
   b=i+k
   if abs(a) in occup:
    print(a)
    val=False
   if abs(b) in occup:
    print(b)
    val=False
   if abs(a) not in occup and abs(b) not in occup:
    ver=verif(occup,i,k)
    print(ver)
    if verif(occup,i,k):
     occup.append(i)
     nbre+=1
  print(occup)
 return nbre
   
tab=[1,2,3,4,5,6,7,8,9,10,11]
k=1
occup=[2,6]
tab1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
occup1=[11,6,14]
k1=2
print(indice(tab,k,occup))
print("second case")
print(indice(tab1,k1,occup1))
print(verif(occup1,1,2))

