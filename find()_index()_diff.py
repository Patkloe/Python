s1 = "just learn string functions"
s2 = "just"
s1.find(s2)      #output 0
s3 = "decouvre"
s1.find(s3)      #output   -1
s.index(s3)      # will raise a python error
# s1.find("texte recherche",deb,fin)   as s1.index()
# index() return the index where the substring starts in the string
#rindex() return the end of index where we have the substring


# sample

tab = "veux decouvrir Python Python"
print(tab.rindex("Python"))
test =tab[4:]
suit =tab[:4]
form1 = test + suit
form2 = suit + test
print(form1)
print(form2)
print(tab.find("veux"))
