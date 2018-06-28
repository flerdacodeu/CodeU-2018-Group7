from map_class import Map

def count_islands(map_):
    n_islands = 0
    visited = [[False for i in range(map_.x_max)] for j in range(map_.y_max)]
    for y in range(map_.y_max):
        for x in range(map_.x_max):
            if map_[(x, y)] and (not visited[y][x]):
                visited = map_.traverse(x, y, visited)
                n_islands += 1
    return n_islands

