def myfunc():
  x = 300    #global
  y = 0
  for i in range(5):
    y = y + 1
  print(i)
  def myinnerfunc():
   #if(i == 5):    variable i it is not visible here
    print(x)
  return myinnerfunc()

myfunc()
