from typing import List


def neighbors(input_array, num_rows, num_cols, x, y):
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            xn, yn = x + dx, y + dy
            if (0 <= xn < num_rows and 0 <= yn < num_cols and
                    input_array[xn][yn]):
                yield xn, yn


def dfs(num_rows, num_cols, input_array, x, y):

    # mark the current tile as visited
    input_array[x][y] = False
    # start dfs from every neighbour of the current tile
    for next_x, next_y in neighbors(input_array, num_rows, num_cols, x, y):
        dfs(num_rows, num_cols, input_array, next_x, next_y)


def count_islands(num_rows, num_cols, input_array: List[bool]):
    """
    Count islands in the given 2d array (List)
    :param input_array: input array, where True is land, False is water
    :return: num of islands
    """

    # go through the input array and count the number of connected components
    num_islands = 0
    for x in range(num_rows):
        for y in range(num_cols):
            # the new connected component is started
            if input_array[x][y]:
                num_islands += 1
                dfs(num_rows, num_cols, input_array, x, y)
    return num_islands


