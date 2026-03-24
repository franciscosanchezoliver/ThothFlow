from thothflow.core.graph import Graph
from thothflow.core.graph import Node


class TestGraph:

    def test_create_graph_with_str_as_nodes(self):

        A = 'A'
        B = 'B'

        graph = Graph()
        graph.add_node(A)
        graph.add_node(B)

        graph.add_edge(A, B)

        print(graph)

    def test_create_graph_with_node_as_nodes(self):

        A = Node("A")
        B = Node("B")

        graph = Graph()
        graph.add_node(A)
        graph.add_node(B)

        graph.add_edge(A, B)

        print(graph)
