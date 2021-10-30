def verif_anagram(a1,a2):
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
print(verif_anagram("paypal","palpay"))
