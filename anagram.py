def isAnagram(str1, str2):
    str1_list = list(str1) # define a list on the first argument
    str1_list.sort()    # sort the list
    str2_list = list(str2) # define a list on the second argument
    str2_list.sort()    # sort the list
    print(str1_list)
    return (str1_list == str2_list)  # return comparison of two list
    
print(isAnagram("paypal1","palpy1"))
val = "Decouvrir un travail"
val_list = list(val)
#print(str1_list)


# a finir
def isAnagram(str1, str2):
 if len(str1)==len(str2):
  dic = dict()
  vrai = True
  for i in range(len(str1)):
   dic[str1[i]] = str1.count(str1[i])
  for j in range(len(str2)):
   if str2[j] in dic and dic[str2[j]]:  # in dic:
    dic[str2[j]] = dic[str2[j]] - 1
   else:
    vrai = False
    break
   #vrai = False
 vrai = True
 print(vrai)
isAnagram("papa","paaf")

 # version 1.0
    def verif_anagram():
 dic = {"a":2,"b":3,"c":4}
 tex = "aabbbccccc"
 for i in range(len(tex)):
  if tex[i] in dic:
   if dic[tex[i]]:
    dic[tex[i]] = dic[tex[i]] - 1
   else:
    return False
  else:
   return False
 return True
print(verif_anagram())

