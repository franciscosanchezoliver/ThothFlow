from typing import Dict, List, Set


class Node:
    def __init__(
        self,
        name
    ):
        self.name = name

    def __repr__(self):
        return f"({self.name})"


class Graph:
    """
    DAG (Directed Acyclic Graph).
    """

    def __init__(self):
        # Each Node has an entry in the dictionary.
        # Each Node has a list of adjacent Nodes (edges).
        self.adjacency: Dict[str, List[str]] = {}

    def add_node(self, node):
        # Only add if the node doesn't already exist.
        if node not in self.adjacency:
            self.adjacency[node] = []

    def add_edge(self, from_node, to_node):
        # Add a connection between nodes.
        self.add_node(from_node)
        self.add_node(to_node)

        self.adjacency[from_node].append(to_node)

    def get_neighbors(self, node):
        return self.adjacency.get(node, [])

    def __repr__(self):
        graph_as_str = str(self.adjacency)
        graph_as_str = graph_as_str.replace(":", "->")
        graph_as_str = graph_as_str.replace("[", "[ ")
        graph_as_str = graph_as_str.replace("]", " ]")
        return graph_as_str
