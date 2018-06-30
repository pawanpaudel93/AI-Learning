from uniform_cost_search import ucs, graph


def astar_search():
    return ucs(graph, 'Arad', 'Bucharest', 'heuristics.txt')
# ucs(graph, 'Arad', 'Bucharest')


astar_search()



