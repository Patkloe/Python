def binaire(n):
 res = ""
 while n > 0 :
  res += str(n%2)
  n//=2
 return res[::-1]
 
print(binaire(8))

"""def decimal(n):
 res = 0
 for i in range[len(str(n))]:
  res = res + 2**int(n[i])
 return res
 
print(decimal(100))"""
  
