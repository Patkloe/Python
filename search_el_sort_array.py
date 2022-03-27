def searchInSorted(self,arr, N, K):
     deb=0
     fin=len(arr)-1
     while deb<=fin:
      mid=(deb+fin)//2
      if arr[mid]>K:
        fin-=1
      elif arr[mid]<K:
        deb+=1
      else:
        return 1
     return -1
