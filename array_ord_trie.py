h=None
print(h)
print(type(h))
mat=[None]*48
strg="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
size=len(strg)
print(size)
for i in range(size):
 mat[ord(strg[i])-ord("a")]=strg[i]
print(mat)

print(ord("a")-ord("a"))
print(ord("A")-ord("a"))

