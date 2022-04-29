#version 1.0
def digit(nbre):
 if (nbre//10)<10:
  return nbre%10,nbre//10
 else:
  return digit(nbre//10)

print(digit(125))
