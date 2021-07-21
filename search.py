def rech(a):
 Tab = [1, 2, 3, 4, 5, 7]
 for x in Tab:
  print(x) 
 size = len(Tab)
 for i in range(size):
  if(Tab[i] == a):
   #print(i)
   print("Trouve")
   break
  if(Tab[i] != a) & (i == size - 1):
   print("fail")
 #if(i == size):
 #print(i)
 #print("fail")
 return 0
rech(7)
