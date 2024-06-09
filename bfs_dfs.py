from collections import defaultdict
class Graph:
 def __init__(self):
  self.graph=defaultdict(list)
 def addedge(self,u,v):
  self.graph[u].append(v)
 def bfs(self,v):
  queue=[]
  visited=[False]*(max(self.graph)+1)
  queue.append(v)
  while queue:
   s=queue.pop(0)
   print(s, end= " ")
   visited[s]=True
   for noeud in self.graph[s]:
    if visited[noeud]==False:
     queue.append(noeud)
     visited[noeud]=True
 def dfsutil(self,visited,v):
  visited.add(v)
  print(v, end=" ")
  for noeud in self.graph[v]:
   if noeud not in visited:
    self.dfsutil(visited,noeud)
 def dfs(self,s):
  visited=set()
  self.dfsutil(visited,s)

     
     
g = Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
 
print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
g.bfs(2)
print("\n")
print("Following is Dept First search"
          " (starting from vertex 2)")
g.dfs(2)
