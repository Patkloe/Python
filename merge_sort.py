#version 001
'''thislist = ["apple", "banana", "cherry"]
n = len(thislist)
l1 = thislist[0:int(n-1/2)]
l2 = thislist[int(n-1/2)::n]
print(thislist)
print(l1)
print(l2)'''
# definir fonction Fusionner(l1,12)

def trier(l):
 n = len(l)
 if n == 0 or n == 1 :
  return l
 else:
  l1 = trier(l[0:int(n-1)/2])
  l2 = trier(l[int(n-1/2):n])
