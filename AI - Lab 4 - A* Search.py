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
def heuristic_table(romania_cities):
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
    }[romania_cities]

def a_star(graph, start, end):
    city_explored = []
    queue = PriorityQueue()
    queue.put((0, start))
    cost = {start: 0}
    path = {start: [start]}

    while not queue.empty():
        # get the node with the lowest f value (cost + heuristic)
        (f, city) = queue.get()
        city_explored.append(city)

        if city == end:
            return (path[city], cost[city])

        for neighbor in graph[city]:
            new_cost = cost[city] + graph[city][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

            # calculate the f value (cost + heuristic) for the neighbor city
                f = new_cost + heuristic_table(neighbor)

            # adding neighbor city to the queue
                queue.put((f, neighbor))

            # update the path to the neighbor city
                path[neighbor] = path[city] + [neighbor]

    return None

start = 'Arad'
end = 'Bucharest'
result = a_star(graph, start, end)

if result is not None:
    path, cost = result
    print("Cities explored by A* Search:", path)
    print("Total cost:", cost)
else:
    print("End city cannot be reached.")