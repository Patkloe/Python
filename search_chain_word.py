def search_chain_word():
 g="amkjhgffffdddd"
 cons=""
 tab=[]
 i=0
 while i<len(g):
  cons+=g[i]
  if len(cons)==4:
   tab.append(cons)
   cons=""
  if len(cons)<=4 and i==len(g)-1:
   tab.append(cons)
  i+=1
 return tab
 
print(search_chain_word())

# search , complexity )(n)
tab=["voila","c'est","mon","anniversaire"]
for i in tab:
 print(i)
 if i=="mon":
  print(tab.index(i))
  break
  #print(tab.index(i))
