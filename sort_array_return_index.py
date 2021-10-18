s = [2, 3,1, 1, 4, 5]  # array to sort
li=[]  # array where we keep element and index
  
for i in range(len(s)):  # loop on array element
      li.append([s[i],i]) # build the array of array (element, index)
print(li) # just to see the array of array built
li.sort() # sort that array
print(li)   # display that array
sort_index = []   #
  
for x in li:
      sort_index.append(x[1])  # index position 1, we get that index in the array of array, then add to the array of index, we want to get at the end.
  
print(sort_index)
print(s[2])  # sample   2 an element of the sort index
