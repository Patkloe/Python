def valid(S):
 val =[]
 i = 0
 while(i < len(S)):
  ma =S[i].upper()
  mi = S[i].lower()
  typ = type(i)
  if(S[i]==ma and "ma" not in val ):
    val.append("ma")
  if(S[i].isdigit() and "ent" not in val):
    val.append("ent")
  if (S[i]==mi and "min" not in val):
    val.append("min")
  i+=1
  if(("ent" in val)and("ma" in val)and("min" in val)):
   print("YES")
  else:
   print("NO")
