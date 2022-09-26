fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x and x=="a":
    newlist.append(x)

print(newlist)

mylist = ['abc123', 'def456', 'ghi789']
sub = 'abc'
test=[sub in mystring for mystring in mylist]
print(test)

test2=[string for string in mylist if string=="ab"]
print(test2)
test3=[string for string in mylist if sub in string]
print(test3)

'''strings_with_substring = [string for string in strings ]
print(strings_with_substring)

if substring in  string'''
