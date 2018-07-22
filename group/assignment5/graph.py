from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def dfs(self, v, visited, order):
        # visited - array of marks for every vertex
        # visited[v] = 0 - v hasn't been visited yet
        #              1 - visited but haven't visited all vertices in it's subtree
        #              2 - all vertices in it's subtree were visited
        visited[v] = 1
        graph_list = self.adjacency_list
        for neighbour in graph_list[v]:
            if not visited[neighbour]:
                if not self.dfs(neighbour, visited, order):
                    return False
            # cycle was found => no topological sort
            elif visited[neighbour] == 1:
                return False
        visited[v] = 2
        order.appendleft(v)
        return True

    def topological_sort(self, v):
        """
        :returns: None if there is no topological sort
        or the list of vertices in topological sort order
        """
        visited = dict.fromkeys(self.vertices, 0)
        order = deque()

        for v in self.vertices:
            if not visited[v]:
                if not self.dfs(v, visited, order):
                    return None
        return list(order)
