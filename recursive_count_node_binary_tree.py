class Nodetree:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None
 def insert(self,val):
  if self.data:
   if val<self.data:
    if self.left is None:
     self.left=Nodetree(val)
    else:
     self.left.insert(val)
   else:
    if self.right is None:
     self.right=Nodetree(val)
    else:
     self.right.insert(val)
  else:
   self.data=val
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

tab=[2,3,4,9,6,1,8,5,7]
test=Nodetree(0)
for j in tab:
 test.insert(j)
print(count_nodes(test))
