def checknum(tab):
 temp=""
 for i in range(len(tab)):
  if tab[i]!="-":
   temp+=tab[i]
 typ=int(temp)
 print(type(typ))
 test=isinstance(typ, int)
 if(test):
  cp=6+2j
  print(type(cp))
  print(type(test))
  return True
 else:
  print(temp)
  print(typ)
  return False
tab="23-25"
print(checknum(tab))
