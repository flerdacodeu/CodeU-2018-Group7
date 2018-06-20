from dictionary import Dictionary
from collections import deque

def is_valid_index(ind, size):
    return (ind >= 0) and (ind < size)

def get_valid_neighbours(position, n_rows, n_cols):
    '''
    Given a position in the matrix returns valid neighbours, i.e. only these
    that are inside the matrix
    '''
    neighbours = list()
    row, col = position
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i != row or j != col) and is_valid_index(i, n_rows) and is_valid_index(j, n_cols):
                neighbours.append((i, j))
    return neighbours

def word_search_with_prefix(grid, dictionary, queue, prefix=None, visited=None):
    '''
    Recursively searches the words from dictionary given a grid and a prefix
    Returns a set of words
    '''
    if prefix is None:
        prefix = ''
    if visited is None:
        visited = set()

    words = set()
    while len(queue) > 0:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        prefix_new = prefix + grid[row][col]
        if not dictionary.is_prefix(prefix_new):
            continue
        if dictionary.is_word(prefix_new):
            words.add(prefix_new)
        visited_new = visited.copy()
        visited_new.add((row, col))
        to_visit = deque(get_valid_neighbours((row, col), len(grid),
            len(grid[0])))
        words = words.union(word_search_with_prefix(grid, dictionary, to_visit, prefix_new, visited_new))
    return words

def word_search(grid, dictionary):
    """
    grid - a matrix, each element is a symbol (assume English alphabet)
    dictionary – a class containing all possible words. should have is_prefix
    and is_word methods
    Returns a set of the words from a given dictionary that can be found in
    a grid
    """
    words = set()
    n_rows = len(grid)
    if n_rows == 0:
        return words
    n_cols = len(grid[0])
    for row in range(n_rows):
        for col in range(n_cols):
            queue = deque([(row, col)])
            words = words.union(word_search_with_prefix(grid, dictionary, queue))
            if len(words) == len(dictionary.words):
                return words
    return words

