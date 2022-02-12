# Python program for implementation of MergeSort      version 0.1
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)           # This version is contributed by Mayank Khanna
    
    
    # version 0.2   contributed by  Patrick Motsebo
    def mergesort(myList):
 if len(myList) > 1:
  mid = len(myList)//2
  left = myList[:mid]
  right = myList[mid:]
  mergesort(left)
  mergesort(right)
  i = 0 # left 
  j = 0 # right
  k = 0 # array sorted
  while i < len(left) and j < len(right):
   if left[i] <= right[j]:
    myList[k] = left[i]
    i = i + 1
   else:
    myList[k] = right[j]
    j = j + 1
   k = k + 1
  while i < len(left):
   myList[k] = left[i]
   i = i +1
   k = k + 1
  while j < len(right):
   myList[k] = right[j]
   j = j + 1
   k = k + 1
  return myList
 else:
  return myList
tab = [6,5,4,9,8,7,3,2,1,0]
print(mergesort(tab))
