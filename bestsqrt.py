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
   
# version 000000.1
def bstsqrt(x):
 import math
 sol=[]
 if x>1:
  for i in range(1,x):
   if math.floor(i*i)<=x:
    sol.append(i)
  return max(sol)
 else:
  return 0

print(bstsqrt(2))
