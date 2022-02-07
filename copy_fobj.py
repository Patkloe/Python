test = "exemple, voir"
ex = list(test)
print(ex)
cop = ex[:]   # we copy the object
print(cop)
ex[0] = "W"   # we modify the source
print(ex)     # source changes
print(cop)    # the copy does not change.
