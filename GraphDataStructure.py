import random

class Graph():
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None
        
    def __contains__(self, key):
        return key in self.vertices
    
    def add_edge(self, from_key, to_key, weight=1):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)
        self.vertices[to_key].add_neighbor(self.vertices[from_key], weight)

    def get_vertices(self):
        return self.vertices.keys()
    
class Vertex():
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight = 1):
        self.neighbors[neighbor] = weight

    def get_connections(self):
        return self.neighbors.keys()
    
    def get_weight(self, neighbor):
        return self.neighbors[neighbor]
    
    def __str__(self):
        return '{} neighbors: {}'.format(self.key, [x.key for x in self.neighbors]) 

def adjacency_lists(graph):
    for key in graph.vertices:
        print(graph.vertices[key])
    
def generate_tree(n):
    tree = Graph()
    for i in range (n): # Creating a vertex for each n
        tree.add_vertex(Vertex(i))

    for i in range(1,n):
        p = random.randint(0, i-1)  # Generate random vertex and add as edge
        tree.add_edge(i, p)
    return tree

def random_edge(graph, k):
    n = len(graph.vertices)

    for i in range(1,k): # Create 2 random vertexes 
        v1 = random.randint(0, n-1)
        v2 = random.randint(0, n-1)
        
        while v1 == v2 or graph.vertices[v1] in graph.vertices[v2].neighbors:  # Checks if they are already neighbors
            v1 = random.randint(0, n-1)
            v2 = random.randint(0, n-1)

        graph.add_edge(v1, v2)

def bfs(v):
    Q = [(v, 0)]  # Implement as queue
    inQueue = [v]
    maxDistance = 0

    while Q:    
        x,distance = Q.pop(0)

        for neighbor in x.neighbors:
            if(neighbor not in inQueue):
                Q.append((neighbor, distance+1))
                inQueue.append(neighbor)

    return distance

def dfs(v):
    S = [(v,0)]  # Implement as a stack 
    visited = [v]
    length = 0
    while S:
        c, distance= S.pop(len(S)-1)
        length+=distance

        for neighbor in c.neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                S.append((neighbor, distance +1))
            
    return length
    
def getDiameter(tree):
    diameter = 0
    for key in tree.vertices:
        temp = bfs(tree.get_vertex(key))
        if temp > diameter:
            diameter = temp
    return diameter

def main():
    
    #Part 2
    n_values = [100,200,300,400,500]
    k = 5
    for n in n_values:
        avgTreeD = 0
        avgGraphD = 0
        for test in range(1, k):
            tree = generate_tree(n)
            treeDiam = getDiameter(tree)

            random_edge(tree, n)
            graphDiam = getDiameter(tree)

            avgTreeD += treeDiam
            avgGraphD += graphDiam

        avgTreeD /= k
        avgGraphD /= k
        print(n, "tree avg: ", avgTreeD, "graph avg: ", avgGraphD)
    '''
    #Part 3
    n_values = [100,200,400,800,1600]
    k = 10
    for n in n_values:
        ratio = 0
        for test in range(1, k):
            tree = generate_tree(n)
            random_edge(tree, n)
            v = random.choice(list(tree.vertices.values()))

            dfsSum = dfs(v)
            bfsSum = bfs(v)

            ratio += dfsSum / bfsSum
        avgRatio = ratio / n

        print('n:',n, end=' ')
        print(avgRatio) '''

main()
