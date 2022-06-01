def bestsqrt(x):
 import math
 sol=[]
 if x>=1:
  for i in range(1,x):
   if math.floor(i*i)<=x:
    sol.append(i)
  return max(sol)
 else:
  return 0
  
print(bestsqrt(16))
   
