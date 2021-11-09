def isPalindrome(s):
 r = s[::-1] # reverse string
 if(s==r):
  return True
 else:
  return False
  
print(isPalindrome("aba"))
def isPalindrome(st):
 if st == st[::-1]:
  return True
 return False
 
 
print(isPalindrome("ratar"))
