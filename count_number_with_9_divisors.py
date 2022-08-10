def divisors(n):
 rep=False
 nbre=0
 for i in range(1,n+1):
  if n%i==0:
   nbre+=1
 if nbre==9:
  rep=True
 return rep
def count_divisor(m):
 nbre=0
 for k in range(0,m+1):
  if divisors(k):
   nbre+=1
 return nbre
print(divisors(90))
print(count_divisor(100))
 
