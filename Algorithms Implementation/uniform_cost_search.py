import queue as Q


def ucs(graph, start, goal, heuristic=None):
    if start not in graph:
        raise TypeError(start + ' not found in graph !')
    if goal not in graph:
        raise TypeError(goal + ' not in graph !')
    if heuristic:
        def get_heuristic_value(node):
            f = open(heuristic)
            while True:
                node_heuristic = f.readline().split()
                if node_heuristic and node == node_heuristic[0]:
                    return int(node_heuristic[1])
                if not node_heuristic:
                    break
    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if goal in node[1]:
            print("Pathfound: " + str(node[1]) + ", Cost= " + str(node[0]))
            break

        if heuristic:
            cost = 0
            if len(node[1]) == 1:
                pass
            elif heuristic:
                ref = start
                for n in node[1][:]:
                    if n == start:
                        continue
                    else:
                        cost += graph[ref][n]
                        ref = n
        else:
            cost = node[0]
        for neighbour in graph[current]:
            temp = node[1][:]
            temp.append(neighbour)
            if heuristic:
                queue.put(((cost + graph[current][neighbour] + get_heuristic_value(neighbour)), temp))
            else:
                queue.put(((cost + graph[current][neighbour]), temp))


graph = {
    'Giurgiu': {'Bucharest': 90},
    'Mehadia': {'Dobreta': 75, 'Lugoj': 70},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Rimnicu_Vilcea': 80, 'Fagaras': 99},
    'Pitesti': {'Bucharest': 101, 'Rimnicu_Vilcea': 97, 'Craiova': 138},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Bucharest': {'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Rimnicu_Vilcea': {'Pitesti': 97, 'Craiova': 146, 'Sibiu': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Craiova': {'Pitesti': 138, 'Dobreta': 120, 'Rimnicu_Vilcea': 146}
}
if __name__ == '__main__':
    ucs(graph, 'Arad', 'Bucharest')
