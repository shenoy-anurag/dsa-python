import random
from typing import List


class Edge:
    def __init__(self, source, target) -> None:
        self.source = source
        self.target = target

    def __str__(self) -> str:
        return "(" + self.source + " : " + self.target + ")"


class AdjacencyRepresenter:
    def __init__(self) -> None:
        self.n = 0
        self.adjacency_list = {}
        self.all_vertices = set()

    def add_edge(self, source, target):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append(target)
        if target not in self.adjacency_list:
            self.adjacency_list[target] = []
        self.adjacency_list[target].append(source)
        self.all_vertices.add(source)
        self.all_vertices.add(target)

    def from_edge_list(self, edge_list: List[Edge]):
        for edge in edge_list:
            self.add_edge(edge.source, edge.target)
        return self.adjacency_list


if __name__ == '__main__':
    edge_list = []
    for i in range(1, 10, 1):
        source = i
        target = random.randint(1, 10)
        edge = Edge(source=source, target=target)
        edge_list.append(edge)

    adjRep = AdjacencyRepresenter()
    adjacency_list = adjRep.from_edge_list(edge_list=edge_list)

    for k, v in adjacency_list.items():
        adjacency_list[k] = list(set(v))
    print(adjacency_list)
