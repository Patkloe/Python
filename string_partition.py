def partition_string():
test="frrddssaewdscxcxcxcxcx"
deb=0
fin=len(test)
temp=""
res=[]
while deb<fin:
 if test[deb] in temp:
  a=deb
  res.append(temp)
  temp=""
  deb=a
 else:
  temp+=test[deb]
  deb+=1
print(res)
 
