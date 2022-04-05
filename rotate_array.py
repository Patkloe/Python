#rotate array by slicing
li=[1,2,3,4,5]
l1=li[2:]
l2=li[:2]
print(l1)
print(l2)
rot=l1+l2
print(rot)
#inverse
inv1=li[-2:]
inv2=li[:-2]
print(inv1)
print(inv2)
invrot=inv1+inv2
print(invrot)
