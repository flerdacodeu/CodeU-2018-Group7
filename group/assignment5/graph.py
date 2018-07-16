from collections import OrderedDict

class Graph():
    def __init__(self):
        self.edges = dict()
        self.vertices = set()

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            return
        self.vertices.add(vertex)
        self.edges[vertex] = list()

    def add_edge(self, from_, to_):
        self.add_vertex(from_)
        self.add_vertex(to_)
        self.edges[from_].append(to_)

    def topological_sort(self):
        colors = dict.fromkeys(self.vertices, 'white')
        time = 0
        exit_times = dict.fromkeys(self.vertices, 0)
        for vertex, color in colors.items():
            if color == 'white':
                try:
                    time = self._dfs(vertex, exit_times, time, colors)
                except ValueError as err:
                    raise ValueError(err)

        order = sorted(exit_times.items(), key=lambda x: x[1])
        return [x[0] for x in order]

    def _dfs(self, vertex, exit_times, time=0, colors=None):
        if colors is None:
            colors = dict.fromkeys(self.vertices, 'white')
        children = self.edges[vertex]
        colors[vertex] = 'gray'
        for child in children:
            if colors[child] == 'white':
                time = self._dfs(child, exit_times, time, colors)
            elif colors[child] == 'gray':
                raise ValueError('There is a cycle in the graph')
        time += 1
        colors[vertex] = 'black'
        exit_times[vertex] = time
        return time
