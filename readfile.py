def readfile():
 f = open("demofile.txt", "r")
 tab=f.read()
 sel=tab.split(" ")
 ban = open("banned.txt","r")
 recban=ban.read()
 dicban=recban.split(" ")
 bantab=dicban.values
 banrec=list(bantab)
 for i in range(len(recban)):
  selban[dicban[i]]=dicban[i]
 for j in sel:
  if j in banrec:
   print("banned_word")
  else:
   print(j)
return " "
