def partitionString(s):
 temp=""
 res=[]
 deb=0
 fin=len(s)
 while deb<fin:
  if temp!="" and s[deb] in temp:
   a=deb
   res.append(temp)
   temp=""
   deb=a
  else:
   temp+=s[deb]
   deb+=1
  if deb==fin and temp!="":
   res.append(temp)
 return len(res)

print(partitionString("abacaba"))
