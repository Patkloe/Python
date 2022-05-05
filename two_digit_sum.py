def digitsSum(N):
    ##Your code here
    conv=str(N)
    size=len(conv)
    sum=0
    for i in range(size):
      sum+=int(conv[i])
    return sum
