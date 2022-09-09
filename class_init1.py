class Node:
 def __init__(self, val1, val2):
  self.prenom=val1
  self.nom=val2
 def sortie(self):
  print("Prenom :")
  print(self.prenom)
  print("Nom :")
  print(self.nom)
  
nouveau=Node("Patrick","Motsebo")
nouveau.sortie()
