ex1="je veux decouvrir Python"
test=set(ex1)
print(test)
#x=test[0]
#print(x)
print(test)
testl=list(ex1)
print(testl)
# Python program to demonstrate
# Accessing of elements in a set
  
# Creating a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
  
# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
  if i=="Geeks":
    print(i+" "+"bingo", end=" ")
  
# Checking the element
# using in keyword
print("Geeks1" in set1)
