#version 001
'''thislist = ["apple", "banana", "cherry"]
n = len(thislist)
l1 = thislist[0:int(n-1/2)]
l2 = thislist[int(n-1/2)::n]
print(thislist)
print(l1)
print(l2)'''
# definir fonction Fusionner(l1,12)

def trier(l):
 n = len(l)
 if n == 0 or n == 1 :
  return l
 else:
  l1 = trier(l[0:int(n-1)/2])
  l2 = trier(l[int(n-1/2):n])
  
  # version 1
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

myList = [54,26,93,17,77,31,44,55,20,5,4,3,2,1]
mergeSort(myList)
print(myList)
