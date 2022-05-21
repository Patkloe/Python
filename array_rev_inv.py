def inver_tab(tab):
 size=len(tab)
 i=-1
 print("Inverse :")
 for i in range(-1,-(size+1),-1):
  print(tab[i],end="")
 print() 
 print("Normal :")
 for x in tab:
  print(x,end = "")
 return tab
tab=[0,1,2,3,4,5,6,7,8,9]
inver_tab(tab)

# using slicing
tab = [1,2,3,4,5,6,7,8,9]
rev=tab[len(tab)-1::-1]
gd=tab[::-1]
print(rev)
