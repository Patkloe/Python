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



# other version :
def language(**args):
    """Demo funciton of arbitrary keyword arguments"""
    for a in args:
        print(a, args[a])
        
language(country="NL", code="+31")
 
# sample
def recup(*args):
 res=[]
 for i in range(len(args)):
  for j in range(i+1,len(args)):
   res.append([args[i],args[j]])
 for x in res:
  print(x[0],x[1],sep="-")
 return res
recup("test","essai","decouv","victoire")

#sample
def recup(*args):
 res=[]
 for i in range(len(args)):
  for j in range(i+1,len(args)):
   res.append([args[i],args[j]])
 for x in res:
  #print(x[0],x[1],sep="-")
  taille1 = len(x[0])
  taille2 = len(x[1])
  print(x[0],x[1],sep="-")
  print(taille1,taille2,sep="-")
 return res
recup("test","essai","decouv","victoire")
