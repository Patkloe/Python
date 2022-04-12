test = "exemple, voir"
ex = list(test)
print(ex)
cop = ex[:]   # we copy the object
print(cop)
ex[0] = "W"   # we modify the source
print(ex)     # source changes
print(cop)    # the copy does not change.
# compare list between list, set, and dictionnaries
test = "exemple, voir"
ex = list(test)
print(ex)
cop = ex[:]   # we copy the object
print(cop)
ex[0] = "W"   # we modify the source
print(ex)     # source changes
print(cop)    # the copy does not change.
print("tableau")
print(cop==ex)
set1={1,2,3}
set2={1,2,3}
print("set")
print(set1==set2)
dict1={1:"a",2:"b",3:"c"}
dict2={1:"a",2:"b",3:"c"}
print(dict1==dict2)
