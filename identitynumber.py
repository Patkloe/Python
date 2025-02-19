def control(x):
 res=False
 cal=0
 ##val=chr(x)
 ttl=x*x
 val=str(ttl)
 print(ttl)
 print(val)
 if len(val)==1:
  print(len(val))
  fnl=int(val)
  if fnl==x:
   res=True
 else:  # ici on calcule
  print("debut")
  for i in val:
   cal+=int(i)
   if cal==x:
    res=True
 return res
def verif(nbre):
 res=[]
 taille=str(nbre)
 if len(taille)==1:
  val=control(nbre)
  if val:
   res.append(nbre)
 else:
  for i in range(nbre):
   if control(i):
    res.append(i)
 return res
 
print(verif(10))
#test
print(control(1))
print(control(9))
print(control(8))
print(control(3))
print(control(10))
