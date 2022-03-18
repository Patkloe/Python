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
# to convert in decimal   ver : 1.0
def decimal(n):
 p=1
 res = 0
 rev = n[::-1]
 for i in rev :
   res = res + p*int(i)
   p = p*2
 return res
 
print(decimal("111"))

# to convert decimal  ver : 1.1

def decimal(n):
 res = 0
 rev = n[::-1]
 for i in range(len(rev)) :
   res = res + (2**i)*int(rev[i])
 return res
 
print(decimal("100"))

