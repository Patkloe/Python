#linkedlist python, add / delete a Node to a position

class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 def __repr__(self):  # returns a string as the representation of the object
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
 def addpos(self,val,pos): # add a node to a specific position
  newnode=Node(val)
  if pos<1:
   print("should start at 1")
  elif pos==1:
   temp=self.head
   newnode.next=self.head
   self.head=newnode
  else:
   temp=self.head
   for j in range(1,pos-1):
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
   return #print("Not find")
  prev.next=temp.next
  temp=None
 
tab=["A","B","C","D","E","F","G","H","J","H","I","J","K","L","M"] 
test=Linkedlist()
for j in tab:
 test.addnode(j)
 
test.addpos("Z",5)
test.delete("W")
print(test)
'''firstnode=Node("A")
secondnode=Node("B")
thirdnode=Node("C")
firstnode.next=secondnode
secondnode.next=thirdnode
test=Linkedlist()
test.head=firstnode
print(test)'''









# implement a linked list python
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
  #nodes.append("None")
  return "->".join(nodes)
 def addnode(self,val):
  ins=Node(val)
  if self.head==None:
   self.head=ins
  else:
   temp=self.head
   while temp.next!=None:
    temp=temp.next
   temp.next=ins
 def addpos(self,val,pos):
  ins=Node(val)
  if pos==0:
   print("insert at least in position 1")
  elif pos==1:
   #ins=Node(val)
   ins.next=self.head
   self.head=ins
  else:
   temp=self.head
   for i in range(1,pos-1):
    if temp!=None:
     temp=temp.next
   if temp!=None:
    ins.next=temp.next
    temp.next=ins
   else:
    print("empty")
  
    
   
tab=["A","B","C","D","E","F","G","H"]
test=Linkedlist()
for i in range(len(tab)):
 test.addnode(tab[i])
test.addpos("V",0)
print(test)
  











class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
testlinklist = LinkedList()
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
testlinklist.head = first_node
print(testlinklist)

############## Test #################
# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Inserts a new element at the given position
  def push_at(self, newElement, position):     
    newNode = Node(newElement) 
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1):
      newNode.next = self.head
      self.head = newNode
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None):
        newNode.next = temp.next
        temp.next = newNode  
      else:
        print("\nThe previous node is null.")

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                 
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#Insert an element at position 2
MyList.push_at(100, 2)
MyList.PrintList() 

#Insert an element at position 1
MyList.push_at(200, 1)
MyList.PrintList()  
