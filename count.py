def compte(x, tab):
 nbre = 0
 for i in tab:
  if i == x:
   nbre +=1
 return nbre
 
print(compte("a","tata"))


# use set to get unique values
words = ['Z', 'V', 'A', 'Z','V']
#dic1 = dict(words)
red = set(words)
print(len(set(words)))
print(red)
#print(dic1)
