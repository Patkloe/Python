
# sample written by Patrick Motsebo for training Purposes
class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 def __repr__(self):
  return self.data
class Linkedlist:
 def __init__(self):
  self.head=None
 def __repr__(self):
  node=self.head
  nodes=[]
  while node is not None:
   nodes.append(node.data)
   node=node.next
  nodes.append("None")
  return "->".join(nodes)
 def addnode(self,val):
  newnode=Node(val)
  if self.head is None:
   newnode.next=self.head
   self.head=newnode
  else:
   temp=self.head
   while temp.next is not None:
    temp=temp.next
   temp.next=newnode
 def addpos(self,val,pos):
   newnode=Node(val)
   if pos<1:
    print("should start at least at 1")
   elif pos==1:
    temp=self.head
    if temp is not None:
     newnode.next=temp
     self.head=newnode
   else:
    temp=self.head
    for i in range(1,pos-1):
     if temp is not None:
      temp=temp.next
    if temp is not None:
     newnode.next=temp.next
     temp.next=newnode
 def delete(self,key):
   temp=self.head
   if temp is not None:
     if temp.data==key:
      self.head=temp.next
      temp=None
   while temp is not None:
    if temp.data==key:
      break
    prev=temp
    temp=temp.next
   if temp is None:
     return
   else:
     prev.next=temp.next
     temp=None
def search(node,val):
 pos=0
 temp=node.head
 if temp is not None:
  if temp.data==val:
   pos+=1
   return pos
 while temp is not None:
  pos+=1
  if temp.data==val:
   return pos
  temp=temp.next
 return "Not found"
   
 
tab=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
test=Linkedlist()
for i in tab:
 test.addnode(i)
test.addpos("Z",5)
test.delete("H")
print(search(test,"Y"))
