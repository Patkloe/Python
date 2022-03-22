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
