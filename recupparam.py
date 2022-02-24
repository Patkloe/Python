def recuppram(*args):
 for i in args :
  print(i)

recuppram("vouloir","effet","decouvrir", "tester", "victoire")

# version to retrieve the number of args

def recuppram(*args):
 for i in args :
  print(i)    
 print(len(args)) # get the number of argument in the function

recuppram("vouloir","effet","decouvrir", "tester", "victoire")
