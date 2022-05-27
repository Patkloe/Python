def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        #myList = list()
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              #myList.append(left[i])
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                #myList.append(right[j])
                j += 1
                # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            #myList.append(left[i])
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            #myList.append(right[j])
            j += 1
            k += 1
        #mergeSort(left)
        #mergeSort(right)
        return myList
tab = [54,26,93,17,77,31,44,55,20,5,4,3,2,1]
print(mergeSort(tab))

    # version 1.0    short
    
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
3 test a revoir
# merge sort, good version.  variable i,j,k initiation apres l'appel recursif de mergesort()
def mergesort(tab):
 if len(tab)>1:
  mid=len(tab)//2
  left=tab[:mid]
  right=tab[mid:]
  mergesort(left)
  mergesort(right)
  i=0
  j=0
  k=0
  while i<len(left) and j<len(right):
   if left[i]<right[j]:
    tab[k]=left[i]
    i+=1
   else:
    tab[k]=right[j]
    j+=1
   k+=1
  while j<len(right):
   tab[k]=right[j]
   j+=1
   k+=1
  while i<len(left):
   tab[k]=left[i]
   i+=1
   k+=1
  return tab
 else:
  return tab

mat=[10,2,3,1,5,7,6,4,9,8,15,12,35,32,30]
print(mergesort(mat))




