class Grid:
    '''
    Grid is initially a 2D array, but I turn all values into Node objects
    and augment them with their neighbors
    '''
    def __init__(self, data):
        # turn values into Node objects
        i = 0
        for row in range(len(data)):
            for elem in range(len(data[row])):
                node = Node(data[row][elem], i, set())
                data[row][elem] = node
                i += 1
        try:        
            # compute neighbors
            for row in range(len(data)):
                for ind in range(len(data[row])):
                    tile = data[row][ind]
                    # find up neighbor
                    if row != 0:
                        tile.neighbors.add(data[row - 1][ind])
                    # find left neighbor
                    if ind != 0:
                        tile.neighbors.add(data[row][ind - 1])
                    # find right neighbor
                    if ind != len(data[row]) - 1:
                        tile.neighbors.add(data[row][ind + 1])
                    # find down neighbor
                    if row != len(data) - 1:
                        tile.neighbors.add(data[row + 1][ind])
            self.data = data
        except IndexError:
            raise IndexError('Different number of tiles in rows')
    
    def find_islands(self):
        '''
        Algorithm:
        1. Iterate over tiles and check if the tile is water or island. Work only with island tiles. 
        2. For the first found island tile initialize the array. 
        3. For each island tile iterate over all islands and find overlap between them and the current tile's neighbors.
        4. If there's an overlap, check if there's some island that can be merged, 
        merge it and remove redundant current island.
        5. If no island to merge, add the tile to the current island, remember that island for merging.
        6. If this tile has no connections to other island, create a separate one.
        '''
        islands = []
        
        for row in self.data:
            for tile in row:
                if tile.val:
                    if islands == []:
                        islands.append([tile])
                    else:
                        part = False 
                        prev_island = False 
                        for island in range(len(islands)):
                            connection = set(islands[island]) & tile.neighbors
                            if len(connection) > 0:
                                if prev_island:
                                    islands[island] = set(islands[island]) | set(prev_island)
                                    islands.remove(prev_island) 
                                else:
                                    part = True 
                                    islands[island].append(tile)
                                    prev_island = islands[island] 
                        if not part:
                            islands.append([tile])
        return islands, len(islands)
        
class Node:
    # node class for values in the grid
    def __init__(self, val, i, neighbors):
        self.val = val
        self.i = i
        self.neighbors = neighbors
    
if __name__ == '__main__':
    grid = Grid([[False, True, False, True], 
                 [True, True, False, False],
                 [False, False, True, False],
                 [False, False, True, False]])
    islands, num = grid.find_islands()
    print('Found so many islands:', num)
    for island in islands:
        print([x.i for x in island])
