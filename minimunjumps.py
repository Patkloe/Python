def minjumps(tab,n):
 if n<=1:
  return 0
 if tab[0]==0:
  return -1
 maxstep=tab[0]
 step=tab[0]
 jumps=1
 for i in range(1,n):
  if i==n-1:
   return jumps
  maxstep=max(maxstep,tab[i]+i)
  step-=1
  if step==0:
   jumps+=1
   if i>=maxstep:
    return -1
   step=maxstep-i
 return jumps
 
tab=[2,6,3,5,7,1,8,9]
n=8
print(minjumps(tab,n))
  
