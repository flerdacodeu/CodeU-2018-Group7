from collections import deque

class Map:
    def __init__(self, map_):
        self.map = map_
        self.x_max, self.y_max = len(map_[0]), len(map_)

    def __getitem__(self, position):
        return self.map[position[1]][position[0]]

    def _neighbours(self, x, y, visited):
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            xn, yn = x + dx, y + dy
            if (0 <= xn < self.x_max and 0 <= yn < self.y_max and (not visited[yn][xn])):
                yield xn, yn
    
    def traverse(self, x, y, visited):
        queue = deque([(x, y)])
        visited[y][x] = True
        while len(queue) > 0:
            x_current, y_current = queue.popleft()
            for x_next, y_next in self._neighbours(x_current, y_current, visited):
                if self[(x_next, y_next)]:
                    queue.append((x_next, y_next))
                    visited[y_next][x_next] = True
        return visited

