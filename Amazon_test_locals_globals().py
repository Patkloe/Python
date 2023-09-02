#User function Template for python3
def compte(tab):
 sum1=0
 for i in range(len(tab)): 
  sum1=sum1+(tab[i]*i)
 #print(sum1)
 return sum1
#tab=[8,3,1,2]
def max_sum(a,n):
 sum=0
 cal=0
 for i in range(n):
  locals()['a%s'%i]=a[i:]+a[:i]
 '''for i in range(n):
  print(locals()['a%s'%i])'''
 for i in range(n):
  #cal=cal+(locals()['a%s'%i][i]*i)
  cal=compte(locals()['a%s'%i])
  if cal>sum:
   sum=cal
 return sum
 #print(sum)
 
