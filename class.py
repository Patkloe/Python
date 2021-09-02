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
