class test:
 def __init__(self):
  print("this is how you start")
 def test_func(self):
  print("This is for the best")
obj=test()
obj.test_func()

''' how we use "self" in python, like "this" in Java
class test:
 def __init__():
  print("this is how you start")
 def test_func(self):
  print("This is for the best")
obj=test()
obj.test_func()

error generated during running time 
Traceback (most recent call last):
  File "./prog.py", line 7, in <module>
TypeError: test_func() takes 0 positional arguments but 1 was given
waiting for an argument when it is defined, that's why we need to use
"self" as the default argument
class test:
 def __init__(self):
  print("this is how you start")
 def test_func(self):
  print("This is for the best")
obj=test()
obj.test_func()

'''
