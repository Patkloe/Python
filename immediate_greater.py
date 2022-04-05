def immediateGreater(self,arr,n,x):
        sol=list()
        for i in range(n):
          if arr[i]>x:
              sol.append(arr[i])
        if len(sol)>0:
          return min(sol)
        else:
          return -1
