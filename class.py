class MyClass:
  x = 5
  def __init__(self,name,age):
   
   self.name = name
   self.age = age
  def imprime(self):
   print("je m'appelle " + self.name + ", j'ai " + str(self.age) + "ans")
y = "Test"
print(MyClass)
print(y)
P1 = MyClass("Patrick",37)
print(P1.x)
P1.imprime()
#print(P1.y)
"""
       Another version
       
       class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + "  " + " I am : " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()
"""
# another version

class Node:
   def __init__(self,data):
    self.right = None
    self.left = None
    self.data = data
   def insert(self,data):
     if self.data:
        if self.data > data:
           if self.left is None:
             self.left = Node(data)
           else:
             self.left.insert(data)
        else:
          if self.right is None:
             self.right = Node(data)
          else:
             self.right.insert(data)
     else:
          self.dat = data
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print("Success recording")
#print(Node(6).right)
