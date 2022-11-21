class Nodetree:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None
 def insert(self,val):
  if self is not None:
   if self.data>val:
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
   self.data=data
def nbrenode(node):
 queue=[]
 count=0
 countl=0
 countr=0
 if node is not None:
  queue.append(node)
  while len(queue)>0:
   temp=queue.pop(0)
   if temp is not None:
    count+=1  #nombre de noeuds de l'arbre
   if temp.left is not None:
    countl+=1  # nombre de noeuds a gauche
    queue.append(temp.left)
   if temp.right is not None:
    countr+=1  # nombre de noeuds a droite
    queue.append(temp.right)
  print(countl)
  print(countr)
  print(1+max(countl,countr)) #taille de l'arbre binaire
  return count
  
test=Nodetree(11)
tab=[2,3,4,7,9,6,5,1,8]
for j in tab:
 test.insert(j)
print(nbrenode(test))

#print node added
class Nodetree:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None
 def insert(self,val):
  if self.data:# is not None:
   if self.data>val:
    if self.left is None:
     self.left=Nodetree(val)
     print(self.left.data)
    else:
     self.left.insert(val)
   else:
    if self.right is None:
     self.right=Nodetree(val)
     print(self.right.data)
    else:
     self.right.insert(val)
  else:
   self.data=data
def nbrenode(node):
 queue=[]
 count=0
 countl=0
 countr=0
 if node is not None:
  queue.append(node)
  while len(queue)>0:
   temp=queue.pop(0)
   if temp is not None:
    count+=1  #nombre de noeuds de l'arbre
   if temp.left is not None:
    countl+=1  # nombre de noeuds a gauche
    queue.append(temp.left)
   if temp.right is not None:
    countr+=1  # nombre de noeuds a droite
    queue.append(temp.right)
  print(countl)
  print(countr)
  print(1+max(countl,countr)) #taille de l'arbre binaire
  return count
  
test=Nodetree(11)
tab=[2,3,4,7,9,6,5,1,8]
for j in tab:
 test.insert(j)
print(nbrenode(test))

#### Binary Tree Datastructure ########
class NodeTree:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None
  
 def insert(self,val):
  if self.data:
   if self.data>val:
    #left
    if self.left is None:
     self.left=NodeTree(val)
     print(self.left.data)
     print("left")
    else:
     self.left.insert(val)
   else: # self.data<val:
    #right
    if self.right is None:
     self.right=NodeTree(val)
     print("right")
     print(self.right.data)
    else:
     self.right.insert(val)
  else:
   self.data=val
   
tab=[1,2,7,8,0,5,6,3,4,9]
test=NodeTree(0)
for j in tab:
 test.insert(j)
