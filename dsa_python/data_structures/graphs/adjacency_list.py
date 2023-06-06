import random
from typing import List

import pyvis.network


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
            self.adjacency_list[source] = set()
        self.adjacency_list[source].add(target)
        if target not in self.adjacency_list:
            self.adjacency_list[target] = set()
        self.adjacency_list[target].add(source)
        self.all_vertices.add(source)
        self.all_vertices.add(target)

    def from_edge_list(self, edge_list: List[Edge]):
        for edge in edge_list:
            self.add_edge(edge.source, edge.target)
        return self.adjacency_list


def get_all_vertices(adj_list):
    keys = list(adj_list.keys())
    all_vertices = []
    for k in keys:
        all_vertices.append(k)
        all_vertices.extend(list(set(adj_list[k])))
    all_vertices = list(set(all_vertices))
    all_vertices.sort()
    return all_vertices


def create_pyvis_network(adjacency_list) -> pyvis.network.Network:
    net = pyvis.network.Network()

    visited = {}
    count = 1
    for k, vertices in adjacency_list.items():
        if k not in visited:
            net.add_node(count, label=str(k))
            visited[k] = count
            count += 1
        for n in vertices:
            if n not in visited:
                net.add_node(count, label=str(n))
                visited[n] = count
                count += 1
            net.add_edge(visited[k], visited[n])

    return net


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
