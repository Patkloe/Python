def Maxtab(tab):
 reserv={}
 maxv=0
 ind=""
 for i in tab:
   if i in reserv:
     reserv[i]+=1
     if reserv[i]>maxv:
      maxv=reserv[i]
      ind=i
   else:
    reserv[i]=1
 print(reserv)
 return i,maxv
print(Maxtab("voici un exemple"))
