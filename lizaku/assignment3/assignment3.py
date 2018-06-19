class Dictionary():
    '''
    I implement the dictionary as a trie. As an input I give an array of words 
    that are then transformed into a trie. isWord and isPrefix are methods of the Dictionary.
    '''
    def __init__(self, data, end='_end_'):
        self._end = end
        self.data = self._make(data)
    
    def _make(self, words):
        # constructing the trie, it's in form of a dictionary (not very efficient though...)
        _end = self._end
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
        return root
    
    def isWord(self, word):
        _end = self._end
        current_dict = self.data
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        else:
            if _end in current_dict:
                return True
            else:
                return False
    
    def isPrefix(self, word):
        current_dict = self.data
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        return True


class Grid():
    '''
    Grid is initially a 2D array, but I turn all values into Node objects
    and augment them with their neighbors
    '''
    def __init__(self, data):
        self.data = self._make(data)
    
    def _make(self, data):
        # turn values into Node objects
        for row in range(len(data)):
            for elem in range(len(data[row])):
                node = Node(data[row][elem])
                data[row][elem] = node
                
        # compute neighbors; seems to be monstrous, I don't know how to make it more elegant
        for row in range(len(data)):
            for let_ind in range(len(data[row])):
                letter = data[row][let_ind]
                up_neighbors = []
                if row != 0:
                    up_neighbors.append(data[row - 1][let_ind])
                    if let_ind != 0:
                        up_neighbors.append(data[row - 1][let_ind - 1])
                    if let_ind != len(data[row]) - 1:
                        up_neighbors.append(data[row - 1][let_ind + 1])
                row_neighbors = []
                if let_ind != 0:
                    row_neighbors.append(data[row][let_ind - 1])
                if let_ind != len(data[row]) - 1:
                    row_neighbors.append(data[row][let_ind + 1])
                down_neighbors = []
                if row != len(data) - 1:
                    down_neighbors.append(data[row + 1][let_ind])
                    if let_ind != 0:
                        down_neighbors.append(data[row + 1][let_ind - 1])
                    if let_ind != len(data[row]) - 1:
                        down_neighbors.append(data[row + 1][let_ind + 1])
                neighbors = up_neighbors + row_neighbors + down_neighbors
                letter.neighbors = neighbors
        return data
    
    def dfs(self, start, vocab):
        '''
        I look for all possible strings in the grid via depth-first search. 
        This is done for every element in the grid individually.
        '''
        if vocab.isPrefix(start.val):
            # maybe the value of a node is a valid word
            yield start.val
        stack = [(start, [start])]
        while stack:
            (node, path) = stack.pop()
            available = set(node.neighbors) - set(path)
            for neighbor in set(node.neighbors) - set(path):
                stack.append((neighbor, path + [neighbor]))
                word = ''.join([i.val for i in path + [neighbor]])
                # check if the word is a prefix, than yield it further
                if vocab.isPrefix(word):
                    yield word
    
    
def find_words(grid, vocab):
    words = set()
    for row in grid.data:
        for letter in row:
            for word in grid.dfs(letter, vocab):
                # if a word is a valied word, than add it to the resulting set
                if vocab.isWord(word):
                    words.add(word)
    return words
            
        
class Node():
    # node class for values in the grid
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
    
    
if __name__ == '__main__':
    grid = Grid([['a', 'a', 'r'], ['t', 'c', 'd']])
    vocab = Dictionary(['a', 'card', 'cart', 'cat', 'car'])
    print(find_words(grid, vocab))
    
