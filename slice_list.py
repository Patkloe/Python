thislist = [1,2,4,5,7,0,8,6]
size = len(thislist)
mid1 = thislist[0:int(size/2)] # slice a list first part
mid2 = thislist[int(size/2):size] # slice the second part
print(thislist)
print(size)
print(mid1)
print(mid2)
print(thislist[::])
print(thislist[-1::-1]) # a partir de (-1) qui est 6 on fait un pas en l'envers pour avoir 8, ainsi de suite.
# [::]  toute la liste
# [x:y] partie de la liste allant de x inclus a y exclu
# [::-1] reverse la liste , 
​txt = [1,2,3,4,5,7,8,9]
tx1 = txt[::]
print(tx1)
tx2 = txt[::2]
print(tx2)
tx3 = txt[:]
print(tx3)
tx4 = txt[0:9:1]
print(tx4)
tx5 = txt[::-1]  # reverse
print(tx5)
