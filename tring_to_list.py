tab2=[]
test="stringtest"
#test.remove("r")
print(test)
tab=list(test) # use list()
tab2.extend(test)# use extend()
print(tab)
print(tab2)
tab3=[*test]# use unpack method
print(tab3)
#use a loop
tab4=[]
for x in test:
 tab4.append(x)
print(tab4)
tab4.remove("t")#remove the first occurence given as argument
print(tab4)
