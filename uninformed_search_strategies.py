def breadth_first_search(root_node):
    if root_node.is_goalState():
        return {'solution_node': root_node}
    frontier = [root_node]
    explored = []
    while frontier:
        node = frontier.pop(0)
        explored.append(node)
        successor_list = node.get_successor()
        for successor in successor_list:
            if not successor:
                continue
            if successor not in explored:
                if successor.is_goalState():
                    return {'solution_node': successor}
                frontier.append(successor)
    return None


def depth_first_search(root_node):
    if root_node.is_goalState():
        return {'solution_node': root_node}
    frontier = [root_node]
    explored = []
    while frontier:
        node = frontier.pop()
        explored.append(node)
        if node.is_goalState():
            return {'solution_node': node}
        successor_list = node.get_successor()
        for successor in reversed(successor_list):
            if not successor:
                continue
            if successor not in explored:
                frontier.append(successor)
    return None


def depth_limit_search(root_node, limit, explored=None):
    if root_node.is_goalState():
        return {'cutoff': False, 'is_solution': True, 'solution_node': root_node}
    elif limit == 0:
        return {'cutoff': True, 'is_solution': False, 'solution_node': None}
    else:
        cutoff_occurred = False
        if not explored:
            explored = []
        explored.append(root_node)
        for successor in root_node.get_successor():
            if not successor:
                continue
            if successor in explored:
                continue
            result = depth_limit_search(successor, limit-1, explored)
            if result['cutoff']:
                cutoff_occurred = True
            elif result['is_solution']:
                return result
        if cutoff_occurred:
            return {'cutoff': True, 'is_solution': False, 'solution_node': None}
        else:
            return {'cutoff': False, 'is_solution': False, 'solution_node': None}