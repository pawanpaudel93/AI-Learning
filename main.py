from uninformed_search_strategies import \
    (breadth_first_search, depth_first_search,
     depth_limit_search)


class Node:
    search_data = int

    def __init__(self, data=None, parent=None):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def insert(self, data):
        if self.data:
            if data < self.data or data == self.data:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def is_goalState(self):
        return self.data == Node.search_data

    def get_successor(self):
        return [self.left, self.right]


if __name__ == "__main__":
    tree_data = [int(x) for x in input('Enter the tree datas? ').split()]
    Node.search_data = int(input('Enter the desired goal node? '))
    root_node = Node()
    for node in tree_data:
        root_node.insert(node)
    # result = breadth_first_search(root_node)
    # result = depth_first_search(root_node)
    result = depth_limit_search(root_node, 2)
    if result['solution_node']:
        print('Is present')
    elif result['cutoff']:
        print('cutoff occurred')
    else:
        print('Not present')
    path = []
    result = result['solution_node']
    while result:
        path.append(result.data)
        result = result.parent
    if path:
        print(path)
