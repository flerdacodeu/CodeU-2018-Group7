from collections import defaultdict
from os.path import commonprefix
 
class Graph:
    def __init__(self, dictionary):
        self.graph = defaultdict(list)
        self.letters = set()
        for first, second in zip(dictionary, dictionary[1:]):
            prefix = commonprefix([first, second])
            first_letter = first[len(prefix)]
            second_letter = second[len(prefix)]
            self.draw_edge(first_letter, second_letter)
            self.letters = self.letters | set(first) | set(second)
 
    def draw_edge(self, x, y):
        self.graph[x].append(y)

    def dfs(self, node, visited, alphabet):
        if node not in visited:
            visited.append(node)
            for n in self.graph[node]:
                if n not in visited:
                    self.dfs(n, visited, alphabet)
        alphabet.insert(0, node)
    
    def topological_sort(self):
        visited = []
        alphabet = []
        for letter in self.letters:
            if letter not in visited:
                self.dfs(letter, visited, alphabet)
        return alphabet

if __name__ == '__main__':
    dictionary = ['ART', 'RAT', 'CAT', 'CAR']
    g = Graph(dictionary)
    alphabet = g.topological_sort()
    print(alphabet)
