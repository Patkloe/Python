def dis_el():
 txt = "je veux decouvrir"
 res = []
 for i in range(len(txt)):
  nbre = txt.count(txt[i])
  if nbre == 1:
   res.append(txt[i])
 return res,set(txt)

print(dis_el())
#version 0.0.1

