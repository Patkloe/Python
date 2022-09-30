def compare(x,y):
 if y-x==1:
  return True
 else:
  return False
def substrlong(s):
 i=0
 temp=[]
 finale=[]
 while i<len(s):
  if i+1<len(s) and compare(s[i],s[i+1]):
   temp.append(s[i])
   temp.append(s[i+1])
  else:
   finale.append(temp)
   temp=[]
  i+=1
 return max(finale)
 
tab=[1,1,2,2,4,4,4,5]
print(substrlong(tab))
