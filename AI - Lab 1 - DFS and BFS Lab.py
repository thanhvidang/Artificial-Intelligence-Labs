#Arad --> Bucharet 
graph = {
    'Arad' : ['Sibiu','Timisoara', 'Zerind'],
    'Sibiu' : ['Arad', 'Fagaras', 'Oradea' , 'Rimnicu Vilcea'],
    'Zerind' : ['Oradea'],
    'Oradea' : ['Zerind', 'Sibiu'],
    'Timisoara' : ['Arad','Lugoj'],
    'Lugoj' : ['Timisoara' , 'Mehadia'],
    'Mehadia' : ['Dobreta', 'Lugoj'],
    'Dobreta' : ['Mehadia', 'Craiova'],
    'Craiova' : ['Dobreta', 'Rimnicu Vilcea' , 'Pitesti'],
    'Pitesti' : ['Craiova', 'Rimnicu Vilcea', 'Bucharest'],
    'Rimnicu Vilcea' : ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras' : ['Sibiu', 'Bucharest'],
    'Bucharest' : []
}

#DFS
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code DFS
print ("This is DFS: ")
dfs(visited, graph, 'Arad')


#BFS - shortest path 
def bfs_shortest_path(graph, start, goal): 
    queue = [[start]] 
    visited = [] 
    while queue:         
        s = queue.pop(0) 
        node = s[-1] #pulling the last node out of the queue
        if node not in visited: 
            for neighbour in graph [node]: 
                new_s = list (s)
                new_s.append(neighbour)
                queue.append(new_s)
                if neighbour == goal: 
                    print("BFS Shortest Path = ", *new_s)
                    return
        visited.append(node)
    return []

# Driver Code BFS
bfs_shortest_path(graph, 'Arad', 'Bucharest') 
