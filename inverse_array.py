# inverse an array following a size,  here we are navigating in the array element, each time we have two elements we reverse their position in a new array.
# noticed, we have a temporary array, when the size of this array equal 2, we are doing some operations, we empty that temporary array ,then the loop on the main array continue
# until we reach the end of the array, if at the end we get a single element, that element will stay at the same position.

tab=[1,2,3,4,5]
cpte=0
temp=[]
res=[]
for i in range(len(tab)):
 cpte+=1
 temp.append(tab[i])
 if cpte==2:
  print(temp)
  res=res+(temp[::-1])
  print(res)
  temp=[]
  cpte=0
 if cpte==1 and i==len(tab)-1:
  res.append(tab[i])
print(res)
  
e1=[1,2,3]
e2=[4,5]
cal=e1+e2
#print(cal)
