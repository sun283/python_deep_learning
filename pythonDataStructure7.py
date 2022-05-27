# [Graph]
# Undirected Graph 
# : relationships are 2-ways(By directional)
# : Used to model social or computer networks.
# : relationships in SNS
# Directed Graph
# : relationships are 1-way.
# : Used to model aireplan flights or bus routes.

# Adjacency List
# : List of neighbors stored in each vertex
# Adjacency Matrix
# : stored 2D array of all the connections between vetices 
# : Matrix of neighbors stored centrally in Graph object

# Undirected Graph
# Adjacency List
# A : B,C,E - Stored in Node A
# B : A,C - Stored in Node B
# C : A,B,D,E
# D : C
# E : A,C
# Adjacency Matrix - Stored in Graph Object
# So each vertex doesn't have to remember its neighbor
# 1 means edge
#      A   B   C   D   E
# A    0   1   1   0   1
# B    1   0   1   0   0
# C    1   1   0   1   1
# D    0   0   1   0   0
# E    1   0   1   0   0
# Weighted Edges?
# Much easier to implement with Adjacency Matrix
# Weighted Edges are used to represent DISTANCE or TIME between nodes.
#      A   B   C   D   E
# A    0   8   9   0   6
# B    8   0   5   0   0
# C    9   5   0   3   1
# D    0   0   3   0   0
# E    6   0   1   0   0
# Directed Graph
# Adjacency List(Outbounded edges)
# A: C
# B: A
# C: B,D,E
# D: None
# E: A
#      A   B   C   D   E
# A    0   0   1   0   0
# B    1   0   0   0   0
# C    0   1   0   1   1
# D    0   0   0   0   0
# E    1   0   0   0   0
# Adjacency List
# Pro: Faster and uses less space for Sparse graphs
# Con: Slower for Dense graphs
# Adjacency Matrix
# Pro: Faster for Dense graphs, Simpler for Weighted edges
# Con: Uses more space

# Vertex Class
# The Vertex class has a constructor that sets the name of the vertex(in our example, just a letter),
# and creates a new empty set to store neighbors.
# The add_neighbor method adds the name of a neighboring vertex to the neighbors set. 
# This set automatically eliminates duplicates.

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()
        
    def add_neighbor(self, v):
        self.neighbors.add(v)
        
# Graph Class
# The Graph class uses a dictionary to store vertices in the format, vertex_name:vertax_object.
# Adding a new vertex to the graph, we first check if the object passed in is a vertex object, 
# then we check if it already exists in the graph.
# If both checks pass, then we add the vertex to the graph's vertices dictionary.
# When adding an edge, we receive two vertx names, we first check if both vertex names are valid,
# then we add each to the others' neighbors set.
# To print graph, we iterate through the vertices, and print each vertex name(the key) followed by its sorted neighbors list.
class Graph:
    # vertices dictionary
    # format = vertex name: vertex object
    vertices = {}
    
    def __init__(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v) # add vertex U as vertex V's neighbor list
            self.vertices[v].add_neighbor(u) # add vertex V as vertex U's neighbor list
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))

# Test code
g = Graph()
# add vertex 3 ways
# 1
a = Vertex('A')
g.add_edge(a)
# 2
g.add_edge(Vertex('B'))
# 3
for i in range(ord('A'), ord('K')):
    g.add_edge(Vertex(chr(i)))
# An edge consists of two vertex names. Here we iterate through a list of edges 
# and add each to the graph
# This print_graph method doesn't give a very good visulaization of the graph, but ti does show
# the neighbors for each vertex.
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', '']
for edge in edges:
    g.add_edge(edge[0], edge[1])
    
g.print_graph()
