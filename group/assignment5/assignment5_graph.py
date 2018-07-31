from collections import defaultdict
from os.path import commonprefix
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.letters = []
        
    def build_from_dictionary(self, dictionary):
        for first, second in zip(dictionary, dictionary[1:]):
            prefix = commonprefix([first, second])
            first_letter = first[len(prefix)]
            second_letter = second[len(prefix)]
            self.draw_edge(first_letter, second_letter)
            for letter in first + second:
                if letter not in self.letters:
                    self.letters.append(letter)
 
    def draw_edge(self, x, y):
        self.graph[x].append(y)

    def dfs(self, node, visited, order):
        if node not in visited:
            visited.append(node)
            for n in self.graph[node]:
                if n not in visited:
                    self.dfs(n, visited, order)
        order.insert(0, node)
    
    def topological_sort(self):
        visited = []
        alphabet = []
        for letter in self.letters:
            if letter not in visited:
                self.dfs(letter, visited, alphabet)
        return alphabet

if __name__ == '__main__':
    dictionary = ['ART', 'RAT', 'CAT', 'CAR']
    g = Graph()
    g.build_from_dictionary(dictionary)
    alphabet = g.topological_sort()
    print(alphabet)
