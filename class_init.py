class decouv:
 def __init__(self,x,y):
  self.name = x
  self.age = y
 def imprime(self):
  print("my name :  " + self.name)
  print("mon age :   " + str(self.age))
t = decouv("patrick",35)
t.imprime()
