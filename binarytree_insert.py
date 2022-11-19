class NodeTree:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None
 def insertnode(self,val):
  #print("start")
  if self.data:
         if val < self.data:
            if self.left is None:
               self.left = NodeTree(val)
            else:
               self.left.insertnode(val)
         elif val > self.data:
            if self.right is None:
               self.right = NodeTree(val)
            else:
               self.right.insertnode(val)
  else:
         self.data = val

def heighttree(node):
 countl=0
 countr=0
 queue=[]
 if node is not None:
  queue.append(node)
  while len(queue)>0:
   temp=queue.pop(0)
   if temp is not None:
    print(temp.data)
   if temp.left is not None:
    countl+=1
    queue.append(temp.left)
   if temp.right is not None:
    countr+=1
    queue.append(temp.right)
 return 1+max(countl,countr)
 
tab=[1,2,7,4,5,6,3,8,9]
test=NodeTree(0)
for i in tab:
 test.insertnode(i)
print(heighttree(test))
