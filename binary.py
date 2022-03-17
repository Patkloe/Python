#Recursive
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
DecimalToBinary(5)
#in built fonction
def decimalToBinary(n):
    return bin(n).replace("0b", "")
print(type(decimalToBinary(4)))
  # other version
  
def binaire(n):
 res = ""
 while n > 0 :
  res += str(n%2)
  n//=2
 return res[::-1]
 
print(binaire(68))

"""def decimal(n):
 res = 0
 for i in range[len(str(n))]:
  res = res + n[i]*2**int(n[i])
 return res
 
print(decimal(100))"""
  
