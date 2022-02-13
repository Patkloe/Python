def reverse(n):
 result = 0       # on initialise result a 0
 while n != 0:     # loop sur n , tant que n different de 0
  result *= 10      #  result est multiplie par 10
  result += n % 10   # a result on ajoute le reste de la division de n par 10
  n //= 10             # n est reduit a la valeur entiere de la division par 10
 return result
 
 # different method

x = 987
t = str(x)
r = list(t)
y = t[::-1]
print(y)
trans = int(y)
print(trans)
