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

# function to get the max value in a string or a list,  then another function to retrieve number of argument for a function

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
print(Maxtab("voici un exemple ici ce en ligne"))

# There is the function to get amount of arguments for a function

def sizearg(*args):
 recup=len(args)
 return recup
print(sizearg("test","developper","bosser","facilite","twitter","observe"))
