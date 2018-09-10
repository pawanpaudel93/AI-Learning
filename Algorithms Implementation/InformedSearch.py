from .uniform_cost_search import ucs, graph


def astar_search():
    return ucs(graph, 'Arad', 'Bucharest', 'Datas/heuristics.txt')


astar_search()