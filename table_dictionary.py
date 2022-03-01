test = {"a":"debut","b":"milieu","c":"fin"}
test["d"] = "profond"
ajout = test.popitem()   # take out the last item inserted in the dictionary
print(ajout)
print(test.get("b"))      # get the item of a key
print(type(ajout))
print(test.pop("a"))
 #tab_pop_append
tab = [1,2,3,4,5,6,7]
tab.append(8)
print(tab)
sort = tab.pop()
print(sort)
print(tab)
print(tab[-1])
ret = tab.pop(0)  # take out the first index of the list
print(ret)
print(tab)
print(0)
a_list = [1, 2, 3]
popped_element = a_list.pop(0)
