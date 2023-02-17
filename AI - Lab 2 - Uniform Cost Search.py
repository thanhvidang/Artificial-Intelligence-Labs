from queue import PriorityQueue

class Graph:
    def __init__(self): 
        self.edges = {}
        self.weights = {}

    def neighbors (self, node):
        return self.edges[node]

    def get_cost (self, from_node, to_node):
            return self.weights [(from_node, to_node)]

graph = Graph()

# Adding nodes and edges to the graph
graph.edges = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Dobreta', 'Lugoj'],
    'Dobreta': ['Craiova', 'Mehadia'],
    'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Dobreta'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu'],
    'Giurgiu': ['Bucharest']
}

# Adding the weights for each edge
graph.weights = {
    ('Arad', 'Zerind'): 75,
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Zerind', 'Oradea'): 71,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Sibiu', 'Oradea'): 151,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Dobreta'): 75,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Pitesti', 'Craiova' ): 138,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Fagaras', 'Bucharest'): 211,
    ('Craiova', 'Dobreta'): 120,
    ('Pitesti', 'Bucharest'): 101,
}

def usc (graph, start, goal): 
    visited = set ()
    queue = PriorityQueue()
    queue.put((0, start))
    path = {start: [start]}

    while queue: 
        cost, node = queue.get()
        if node not in visited: 
            visited.add(node)

            if node == goal: 
                return path[node]
            for i in graph.neighbors(node): 
                if i not in visited: 
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))
                    path[i] = path[node] +[i] 
    return

print(usc(graph, 'Arad', 'Bucharest'))

        
