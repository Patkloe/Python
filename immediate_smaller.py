def immediateSmaller(self,arr,n,x):
        #return required ans
        tab=list()
        for i in range(n):
          if arr[i]<x:
           tab.append(arr[i])
           #print(tab)
        if len(tab)>0:
         return max(tab)
        else:
         return -1
