def merge(l1,l2):
 i = 0
 j = 0
 size1 = len(l1)
 size2 = len(l2)
 res = []
 #while i<size1 & j<size2:
  #if l1[i] < l2[j]:
   #res.append(l1[i])
   #i = i + 1
  #else:
   #res.append(l2[j])
   #j = j+ 1
 while i < size1:
  res.append(l1[i])
  i = i + 1
 while j < size2:
  res.append(l2[j])
  j = j+ 1
 return res
 
tab1 = [2,3,5,6,7]
tab2 = [1,9,6,8,4,0]
print(merge(tab1,tab2))
