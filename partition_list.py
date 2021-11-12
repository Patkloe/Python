def trier(l):    # function definition
 n = len(l)      # size of the list
 if n == 0 | n == 1 : # if the size is 0 or 1
  return l      # return that list
 else:          # otherwise
  l1 = trier(l[0:int(n-1)/2])  # first partition
  l2 = trier(l[int(n-1/2):n])  # second partition
  # here we integrate "fusionner" function     we have merge_sort algorithm
