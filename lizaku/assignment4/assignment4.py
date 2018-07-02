import itertools

class Grid:
    '''
    Grid is initially a 2D array, but I turn all values into Node objects
    and augment them with their neighbors
    '''
    def __init__(self, data):
        # if the user provides the grid that is not valid
        
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
                    # dinf up neighbor
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
        islands = []
        # I iterate over tiles
        for row in self.data:
            for tile in row:
                # if tile is False then this is water, and I do not need to do anything
                if tile.val:
                    # for the first found island tile I initialize the array
                    if islands == []:
                        islands.append([tile])
                    else:
                        part = False # check if this tile is already part of some islands to not create double islands
                        prev_island = False # check if I need to merge this island with some other one
                        for island in range(len(islands)):
                            # iterate over all islands and find overlap between them and the current tile's neighbors
                            connection = set(islands[island]) & tile.neighbors
                            # if there's an overlap
                            if len(connection) > 0:
                                # check if I have some island with which I can merge: ex., [1, 2, 3] and [4, 2] 
                                if prev_island:
                                    islands[island] = set(islands[island]) | set(prev_island)
                                    islands.remove(prev_island) # remove redundant island because it is stored in the merged one
                                else:
                                    # I don't have any islands to merge, but I found a connection anyway
                                    part = True # remember that this tile is part of some island, add it 
                                    islands[island].append(tile)
                                    prev_island = islands[island] # remember the created island for merging
                        if not part:
                            # if this tile has no connections to other islands, create a separate one
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
