class vertex:
    def __init__(self,n):
	self.name=n
	self.neighbours=list()

    def add_neighbour(self,v):
	if v not in self.neighbours:
	    self.neighbours.append(v)
	    self.neighbours.sort()

class Graph:
    vertices={}
    
    def add_vertex(self,v):
	if isinstance(v,vertex) and v.name not in self.vertices:
	    self.vertices[v.name]=v
	    return True
	else:
	    return False

    def add_edge(self,u,v):
	if u in self.vertices and v in self.vertices:
	    for key,value in self.vertices.items():
		if key == u:
		    value.add_neighbour(u)
		if key == v:
		    value.add_neighbour(v)
	    return True
	else:
	    return False

    def print_graph(self):
	for key in sorted(list(self.vertices.keys())):
	    print(key +str(self.vertices[key].neighbours))

g= Graph()


#for i in range(ord('A'),ord('K')):
A= vertex('A')
g.add_vertex(A)
B= vertex('B')
g.add_vertex(B)
C= vertex('C')
g.add_vertex(C)
D= vertex('D')
g.add_vertex(D)

edges = ['AB','AE','AD','BF','CG','DE','DH','EH','FG','FI','GJ','FJ','HI']
#for edge in edges:
g.add_edge(A,B)
g.add_edge(A,C)
g.add_edge(A,D)
g.add_edge(B,C)
g.print_graph()

