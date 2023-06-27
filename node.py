class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 def __repr__(self):
  return self.data
  
a=Node("A")
print(a)

# this is just an sample to create and represented a Node in Python

#sample 2
class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 def __repr__(self):
  return self.data

a=Node("1")
b=Node("2")
a.next=b
print(a)
print(a.next.data)

