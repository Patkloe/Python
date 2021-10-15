test = ['a','b','c','a','d','c']
#nbre = test.count('a')
#char = str(test)
#print(nbre)
nouv = {}   # on initialise un dictionnaire qui va recuperer le nombre d'occurence d'un caractere dans la chaine
for j in test: # pour chaque charactere dans la chaine, le dictionnaire
 nouv[j] = test.count(j) # on compte le nombre d'apparitions dans la chaine on aura pour cle dans le dictionnaire le caharactere et pour valeur, le nombre d'occurence dans la chaine.
print(nouv)

# exercise

given a string, we will print a string with the number of times each character appears in the given string

test = "sdstdstydt  dfgdfgshg"
def const(val): # function to build dictionary
 dic = {}
 for i in val:
  dic[i] = val.count(i) # count each occurence in the string will be the value of the key in the dictionnary
 print(dic)
 return dic
def ecrire(x): # function to get the dictionnary, extract keys and values
 u = list(x.keys()) # extract keys cast the return as a list
 v = list(x.values()) # extract values cast the return as a list
 a = len(u)
 b = len(v)
 print(f"{a} keys")
 print(f"{b} values")
 f = ""
 for k in range(a):
  val = v[k]
  while val > 0:
   f = f + u[k]
   val = val - 1
 print(f) 
  
ecrire(const(test))
