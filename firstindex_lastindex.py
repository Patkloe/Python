# input list need to be sorted
def firstindex(tab,i):
 result=-1
 low=0
 high=len(tab)-1
 while low<=high:
  mid=(low+high)//2
  if tab[mid]<i:
   low=mid+1
  else:
   result=mid
   high=mid-1
  #return 
 return result

#tab= [2,1, 5, 5, 5, 6, 6, 8, 9, 9, 1]
#i=6
#print(firstindex(tab,i))
def lastindex(tab,i):
 result=-1
 low=0
 high=len(tab)-1
 while low<=high:
  mid=(low+high)//2
  if tab[mid]==i:
   result=mid
   low=mid+1
  elif tab[mid]>i:
   high=mid-1
  else:
   low=mid+1
 return result

tab= [1,2,1,2,3,1, 1,5, 5, 5, 6, 6, 8, 9, 9, 9]
i=1
print(firstindex(tab,i))
print(lastindex(tab,i))
