test = [1,2,3,4,5]
ind_tab = []
#val = len(test)
for i in range(len(test)):
 ind_tab.append([test[i],i])
print(ind_tab)
ind = []
for x in ind_tab:
 ind.append(x[1])
print(ind)
