test = "pourterenverser"
unp=[*test]  #unpack to get a list, or we can also use constructor list()
rev=unp[::-1] # reverse by using slicoing method
res="".join(rev) # to join elements of a list.
print(res)
