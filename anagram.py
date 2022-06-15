def isAnagram(a1,a2):
 dic = dict()
 for i in range(len(a1)):
  dic[a1[i]] = a1.count(a1[i])
 for j in range(len(a2)):
  if a2[j] in dic: # on teste que la valeur se trouve dans le dictionnaire
   dic[a2[j]] = dic[a2[j]] - 1 # si c'est le cas on soustrait d'une occurence
   print(dic) # test pour voir le deroulement
   if dic[a2[j]] < 0: # si cette cle existe et est negative, on retourne Faux
    return False
  else:
   return False
 return True
print(isAnagram("paypal","palpay"))

# other version, without using built fonctions

def anagram(x,y):
 garde={}
 if len(x)==len(y):
  for i in x:
   if i in garde:
    garde[i]+=1
   else:
    garde[i]=1
  for j in y:
   if j in garde and garde[j]>0:
    garde[j]-=1
   else: 
    return False
  return True
 else:
  return False
  
print(anagram("vanille","lleniva"))
    
