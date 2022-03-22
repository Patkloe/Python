https://moonbooks.org/Articles/Comment-supprimer-une-%C3%A9l%C3%A9ment-dune-liste-avec-python/
tab = [ "a","b","c","d","e"]
del tab[tab.index("a")]
print(tab)
tab.remove("d")
print(tab)
tab.pop(2)
print(tab)
del tab[:]
print(tab)

# pour faire just a test

'''tab = [ "a","b","c","d","e"]
del tab[tab.index("a")]
print(tab)
tab.remove("d")
print(tab)
tab.pop(2)
print(tab)
del tab[:]
print(tab)
tab.insert(0,"je veux decouvrir")
tab.insert(1, "Cyrielle is my dream")
tab.insert(2, "Python test")
print(tab)
del tab[:]
print(tab)
'''
# delete white space
sentence = ' hello  apple  '
sentence.strip()
print(sentence)
dec = sentence.split(" ")
#sentence.remove(' ')
print(dec)
del dec[2]
print(dec)
nouv ="".join(dec)
print(nouv)
