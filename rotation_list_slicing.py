tab=[1,2,3,4]
tab1=tab[1:]+tab[0:1]
tab2=tab[2:]+tab[0:2]
tab3=tab[3:]+tab[0:3]
print(tab)
print(tab1)
print(tab2)
print(tab3)

#dynamic variable name

for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'
# strg0 = 'Hello', strg1 = 'Hello' ... strg6 = 'Hello'

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"


print(variable16)
print(strg0)

# static
tab=[1,2,3,4]
tab1=tab[1:]+tab[0:1]
tab2=tab[2:]+tab[0:2]
tab3=tab[3:]+tab[0:3]
print(tab)
print(tab1)
print(tab2)
print(tab3)

age = 23


globals()['age'] = 25   # here it is a variable static
print('The age is:', age)
