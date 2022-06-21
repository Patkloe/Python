fop=open("alphanumeric.c","r")
res=fop.read()
print(res)
print(len(res))
print(type(res))
tab=res.split(" ")
print(tab)
print(len(tab))
for i in tab:
    if i=='passed':
     print("success")
     break
