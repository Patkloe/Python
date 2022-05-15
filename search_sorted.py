def search(*arg):
 tab=[]
 for x in arg:
  tab.append(x)
 print(tab)
 return tab
search('tu', 'dis', 'que','quoi', 'un' ,'test')
def mergesort(tab):
 if len(tab)>1:
  mid=(len(tab))//2
  left=tab[:mid]
  right=tab[mid:]
  mergesort(left)
  mergesort(right)
  i=0 #left
  j=0 #right
  k=0 #tab
  while i<len(left) and j<len(right):
   if left[i]<right[i]:
    tab[k]=left[i]
    i=i+1
   else:
    tab[k]=right[j]
    j=j+1
   k=k+1
  while i<len(left):
   tab[k]=left[i]
   i=i+1
   k=k+1
  while j<len(right):
   tab[k]=right[j]
   j=j+1
   k=k+1
  return tab
 else:
  return tab
res=search('aa', 'ab', 'ac','ad', 'ae' ,'aaaf')
print(mergesort(res))
print("test">"quoi")
