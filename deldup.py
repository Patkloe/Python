def deldup(x):
 res = {}
 for i in x :
  res[i] = i
 return res
tab = [1,2,3,4,1,5]
test = deldup(tab)
print("petit test")
