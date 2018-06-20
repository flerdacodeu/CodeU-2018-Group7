from typing import List


class Grid:
    def __init__(self, cells: List[List[str]]):
        self.cells = cells
        self.num_rows = len(cells)
        self.num_cols = 0 if not cells else len(cells[0])

    def neighbours(self, i, j):
        """
        Get all valid neighbours for the given cell
        """

        res = []
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if not (x == i and y == j) and\
                        0 <= x < self.num_rows and 0 <= y < self.num_cols:
                    res.append((x, y))
        return res


def _collect_words(grid, dictionary, i, j, used=None, prefix=""):
    """
    Collect words that begin from the given cell recursively
    """

    words = set()
    cells = grid.cells
    if used is None:
        used = set()
    used.add((i, j))
    prefix += cells[i][j]
    if dictionary.is_word(prefix):
        words.add(prefix)

    # go through all valid neighbours of the given cell to collect more words
    if dictionary.is_prefix(prefix):
        for x, y in grid.neighbours(i, j):
            if (x, y) not in used and dictionary.is_prefix(prefix + cells[x][y]):
                words.update(_collect_words(grid, dictionary, x, y, used, prefix))
    return words


def search_words(grid, dictionary):
    """
    Search words from the given dictionary in the grid
    :param dictionary:
    :return: set of words
    """

    words = set()
    for i in range(grid.num_rows):
        for j in range(grid.num_cols):
            words.update(_collect_words(grid, dictionary, i, j))
    return words
