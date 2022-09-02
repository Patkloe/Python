
# iterative
def somme(n):
  sum=0
  while n>0:
   sum+=n
   n-=1
  return sum
  
print(somme(10))
# recursive
def recsomme(n):
 if n==1:
  return n
 else:
  return n+recsomme(n-1)
  
print(recsomme(10))
  
