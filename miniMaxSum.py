def miniMaxSum(arr):
    # Write your code here
  max=min=0
  temp=sorted(arr)
  for i in range(0,len(temp)-1):
    min+=temp[i]
  rev=temp[::-1]
  for j in range(0,len(rev)-1):
    max+=rev[j]
  print(str(min)+" "+str(max))
