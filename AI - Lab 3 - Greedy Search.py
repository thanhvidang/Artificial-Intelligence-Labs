from queue import PriorityQueue

# map the roads between cities and their distances
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

# calculate the heuristic cost (estimated cost) between a city and Bucharest
def heuristic_table(city):
    return {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Dobreta': 242,
        'Craiova': 160,
        'Rimnicu': 193,
        'Fagaras': 176,
        'Pitesti': 100,
        'Bucharest': 0
    }[city]

def greddy_search (graph, start, end):
    city_explored = []
    queue = PriorityQueue()
    queue.put((heuristic_table(start), start))
    path = {start: [start]}

    while not queue.empty():
        (cost, city) = queue.get()
        city_explored.append(city)

        if city == end:
            return path[city]

        for neighbor in graph[city]:
            if neighbor not in city_explored:
                queue.put((heuristic_table(neighbor), neighbor))
                path[neighbor] = path[city] + [neighbor]
    return None


start = 'Arad'
end = 'Bucharest'
result = greddy_search (graph, start, end)
cost = sum(graph[result[i]][result[i+1]] for i in range(len(result) - 1))

if result is not None:
    print("Cities explored by Greedy Best First Search:", result)
    print ("Total Cost: ", cost)
else:
    print("End city cannot be reached.")    
