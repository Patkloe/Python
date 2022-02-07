mat = [ 1,2,3,4,4,7,2,1]
print(len(mat))
dict_test = dict()
for i in range(len(mat)):
 dict_test[mat[i]] = mat[i]
print(dict_test)
print(dict_test.values())
