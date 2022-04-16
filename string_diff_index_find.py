print("Hello, World!")

test = "pourterenverser"
unp=[*test]
rev=unp[::-1]
res="".join(rev)
print(res)
voir="testisagoodthing"
ins="tisag"
a = ins  not in voir
print(a)
print(ins.find("b")) #find does not raise an error
print(ins.index("b")) # raise an error
