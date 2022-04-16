def compteoccurence():
 testsampl="aaanmaab"
 rech="a"
 nbre=0
 compte=testsampl.find(rech)
 #print(compte)
 while compte>=0:
  nbre+=1
  compte=testsampl.find(rech,compte+1)
 print(nbre)
compteoccurence()
