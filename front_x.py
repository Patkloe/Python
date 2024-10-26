tab=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
res=[]
for y in tab:
 if y[0]=="x":
  res.append(y)
  tab.remove(y)
print(res)
print(tab)
srt1=sorted(res)
srt2=sorted(tab)
srt=srt1+srt2
print(srt)
