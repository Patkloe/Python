def test(*args):
 val = set()
 for i in args:
  val.add(i)
 return val
 
print(test("voir","essai","you","they"))
