from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)

addEdge(graph,'a','c') 
addEdge(graph,'b','c') 
addEdge(graph,'b','e') 
addEdge(graph,'c','d') 
addEdge(graph,'c','e') 
addEdge(graph,'c','a') 
addEdge(graph,'c','b') 
addEdge(graph,'e','b') 
addEdge(graph,'d','c') 
addEdge(graph,'e','c') 

def find_path(graph, start, end, path =[]): 
  path = path + [start] 
  if start == end: 
    return path 
  for node in graph[start]: 
    if node not in path: 
      newpath = find_path(graph, node, end, path) 
      if newpath:  
        return newpath 
      

print find_path(graph,'a','b')
