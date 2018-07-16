class Graph():
    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            return
        self.vertices.append(vertex)
        self.edges.append(list())

    def add_edge(self, from_, to_):
        if from_ not in self.vertices:
            self.vertices.append(from_)
        if to_ not in self.vertices:
            self.vertices.append(to_)
        index_from = self.vertices.index(from_)
        index_to = self.vertices.index(to_)
        self.edges[index_from].append(index_to)

    def topological_sort(self):
        colors = ['white' for i in range(len(self.vertices))]
        time = 0
        exit_times = [0 for i in range(len(self.vertices))]
        for ind, color in enumerate(colors):
            if color == 'white':
                try:
                    time = self._dfs(ind, exit_times, time, colors)
                except ValueError as err:
                    raise ValueError(err)

        order = sorted(zip(self.vertices, exit_times), key=lambda x: x[1])
        return [x[0] for x in order]

    def _dfs(self, vertex_ind, exit_times, time=0, colors=None):
        if colors is None:
            colors = ['white' for i in range(len(self.vertices))]
        children = self.edges[vertex_ind]
        colors[vertex_ind] = 'gray'
        for child in children:
            if colors[child] == 'white':
                time = self._dfs(child, exit_times, time, colors)
            elif colors[child] == 'gray':
                # CYCLE
                raise ValueError('There is a cycle in the graph')
        time += 1
        colors[vertex_ind] = 'black'
        exit_times[vertex_ind] = time
        return time
