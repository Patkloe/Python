def dis_el():
 txt = "je veux decouvrir"
 res = []
 for i in range(len(txt)):
  nbre = txt.count(txt[i])
  if nbre == 1:
   res.append(txt[i])
 return res

print(dis_el())
