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
