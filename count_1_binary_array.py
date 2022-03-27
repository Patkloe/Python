def countOnes(self,arr, N):
        #Your code here
       low = 0
       high = N - 1
       while low <= high:
           mid = (low+high)//2
           if (arr[mid] < 1):
               high = mid - 1
           else:
               if (mid == N - 1 or arr[mid + 1] != 1):
                   return mid + 1
               else:
                   low = mid + 1
       return 0
