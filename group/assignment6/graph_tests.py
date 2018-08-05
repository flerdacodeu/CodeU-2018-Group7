import unittest
from path_finder import Graph


def build_graph_from_pairs(pairs):
    graph = Graph()
    for pair in pairs:
        graph.add_edge(pair[0], pair[1])
        graph.add_edge(pair[1], pair[0])
    return graph


class GraphTest(unittest.TestCase):
    def test_two_vertices(self):
        graph = build_graph_from_pairs(['AB'])
        self.assertEqual(list(graph.find_all_paths('A', 'B')), [['A', 'B']])

    def test_square(self):
        graph = build_graph_from_pairs(['AB', 'BD', 'DC', 'CA'])
        result = sorted(list(graph.find_all_paths('A', 'D')))
        self.assertEqual(result,
                         sorted([['A', 'B', 'D'], ['A', 'C', 'D']]))
        result = sorted(list(graph.find_all_paths('A', 'C')))
        self.assertEqual(result,
                         sorted([['A', 'C'], ['A', 'B', 'D', 'C']]))

    def test_complete_graph_4(self):
        graph = build_graph_from_pairs(['AB', 'AC', 'AD', 'BC', 'BD', 'CD'])
        result = sorted(list(graph.find_all_paths('A', 'D')))
        self.assertEqual(result,
                         sorted([['A', 'D'], ['A', 'B', 'D'],
                                 ['A', 'C', 'D'], ['A', 'B', 'C', 'D'],
                                 ['A', 'C', 'B', 'D']]))

    def test_complete_graph_5(self):
        graph = Graph()
        for v1 in 'ABCDE':
            for v2 in 'ABCDE':
                if v1 != v2:
                    graph.add_edge(v1, v2)

        result = sorted(list(graph.find_all_paths('A', 'D')))
        self.assertEqual(len(result), 16)

    def test_three_vertices(self):
        graph = build_graph_from_pairs(['AB', 'BC'])
        self.assertEqual(list(graph.find_all_paths('A', 'C')),
                         [['A', 'B', 'C']])

    def test_six_vertices(self):
        graph = build_graph_from_pairs(
            ['AB', 'AC', 'AD', 'AE', 'FB', 'FC', 'FD', 'FE'])
        result = sorted(list(graph.find_all_paths('A', 'F')))
        self.assertEqual(result,
                         sorted([['A', 'B', 'F'], ['A', 'C', 'F'],
                                 ['A', 'D', 'F'], ['A', 'E', 'F']]))

    def test_complete_graph_6(self):
        graph = Graph()
        for v1 in 'ABCDEF':
            for v2 in 'ABCDEF':
                if v1 != v2:
                    graph.add_edge(v1, v2)
        result = sorted(list(graph.find_all_paths('A', 'D')))
        self.assertEqual(len(result), 65)

    def test_resistance(self):
        graph = build_graph_from_pairs(
            ['AB', 'BC', 'BD', 'CE', 'DE', 'EF', 'AG'])
        result = sorted(list(graph.find_all_paths('A', 'F')))
        self.assertEqual(result,
                         sorted([['A', 'B', 'C', 'E', 'F'],
                                 ['A', 'B', 'D', 'E', 'F']]))

    def test_two_complete_graphs(self):
        graph = Graph()
        for v1 in 'ABCDEF':
            for v2 in 'ABCDEF':
                if v1 != v2:
                    graph.add_edge(v1, v2)
        for v1 in 'abcde':
            for v2 in 'abcde':
                if v1 != v2:
                    graph.add_edge(v1, v2)
        graph.add_edge('A', 'a')
        result = sorted(list(graph.find_all_paths('C', 'e')))
        self.assertEqual(len(result), 65 * 16)

if __name__ == '__main__':
    unittest.main()
