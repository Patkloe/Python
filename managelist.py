rep=["patrick","papa","pacha","patriarche","mum","wife"]
sol=[]
for x in rep:
 #if x.startswith("pat"):
 if x[:3]=="pat":
  sol.append(x)
print(sol)
