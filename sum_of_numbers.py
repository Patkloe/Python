# sum of number recursive solution
def sum(n):
 if n == 1:
  return 1
 return sum(n - 1) + n
a = sum(10)
print(a)
# sum of numbers with a loop
def boucle(m):
 b = 0
 while m > 0:
   b = b + m
   m = m - 1
 return b
x = boucle(10)
print(x)
