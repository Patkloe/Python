# version 0.0.0.1
def test_val():
 test = [1,2,3,4,5,3,2,6,1,7,8]
 el_dict = {}
 tab = []
 for i in range(len(test)):
  #el_dict[test[i]] = test.count(test[i])
  if test.count(test[i]) == 1:
   tab.append(test[i])
 return tab

print(test_val())
