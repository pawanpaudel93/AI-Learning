def greedy_bfs(source, goal, path=[]):
    is_finished = False
    if source == goal:
        return 'The source state is goal'
    path.append(source)
    neighbour_nodes = get_neighbour_nodes(source)
    value_list = []
    if neighbour_nodes:
        for neighbour in neighbour_nodes:
            if not neighbour:
                continue
            if neighbour == goal:
                path.append(neighbour)
                is_finished = True
            value_list.append(get_heuristic_value(node=neighbour))
    if value_list:
        next_node = get_heuristic_value(value=int(min(value_list)))
        value_list.clear()
        if not is_finished:
            greedy_bfs(next_node, goal, path)
        else:
            for p in path:
                print(p, end=" -> ")
    else:
        print('Please Insert The correct heuristic.txt to reach goal from source')


def get_heuristic_value(node=None, value=None):
    f = open('heuristics.txt')
    while True:
        node_heuristic = f.readline().split()
        if node_heuristic and node == node_heuristic[0]:
            return node_heuristic[1]
        elif node_heuristic and value == int(node_heuristic[1]):
            return node_heuristic[0]
        if not node_heuristic:
            break


def get_neighbour_nodes(node):
    f = open('map.txt')
    while True:
        connected_nodes = f.readline().split()
        if connected_nodes and node == connected_nodes[0]:
            connected_nodes.pop(0)
            return connected_nodes
        if not connected_nodes:
            break


greedy_bfs('Arad', 'Bucharest')