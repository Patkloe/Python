# basic   version 0.01
def isPalindrome(a,b):
 if a==b:
  return True
 return False
#print(isPalindrome("yes","yes"))
tab = "anaba"
deb = 0
fin = len(tab)-1
while deb!=fin:
 if(isPalindrome(tab[deb],tab[fin])):
  deb = deb + 1
  fin = fin - 1
 else:
  print("Not palindrome")
  break
print("Palindrome")
 
