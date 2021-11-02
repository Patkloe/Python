def isPalindrome(s):
 r = s[::-1] # reverse string
 if(s==r):
  return True
 else:
  return False
  
print(isPalindrome("aba"))
