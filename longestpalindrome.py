def isPalindrome(a,b):  # pour checker que nous avons bel et bien un palindrome
 if a == b:
  return True
 return False

def pallong(tab):
 deb = 0      
 fin = len(tab) - 1
 nbre = 0
 res = []
 while deb < fin:
  if isPalindrome(tab[deb],tab[fin]):
   nbre = nbre + 1 # compte le nombre de fois il valide palindrome
   deb = deb + 1   # fait avancer deb a la prochaine occurence
   fin = fin - 1   # fait reculer fin a l'occurence precedente
  res.append(nbre) # on enregistre le nombre dans le tableau
  if not isPalindrome(tab[deb],tab[fin]): # si ce n'est palindrome
   nbre = 0        # on reinitialise nbre
   deb = deb + 1   # avance prochaine occurence
   fin = fin - 1   # recule precente occurence
 return max(res)   # a la fin on retourne la valeur maximale du tableau des nombres de palindromes trouves
  
print(pallong("nancvpapamapapbhnan"))
