from typing import Dict

# from collections import deque
from queue import Queue

from dsa_python.data_structures.graphs.adjacency_list import (
    AdjacencyRepresenter, Edge, get_all_vertices, create_pyvis_network
)
# from dsa_python.data_structures.queue import Queue


class BFS:
    def __init__(self, num_vertices, adjacency_list: Dict) -> None:
        self.N = num_vertices
        self.adj_list = adjacency_list
        self.visited = set()
        self.queue = Queue()
        self.parents = {}
        self.path_traversed = []

    def bfs(self, vertex):
        self.queue.put(vertex)
        while not self.queue.empty():
            v = self.queue.get()
            if v in self.visited:
                self.path_traversed.append((v, 'visited'))
                continue
            
            self.path_traversed.append((v, 'new'))
            self.visited.add(v)  # Mark the vertex as traversed

            adj_vertices = self.adj_list.get(v)
            for n in adj_vertices:
                self.queue.put(n)

                if n not in self.visited:
                    self.parents[n] = v
        return


if __name__ == '__main__':
    edge_list = [
        Edge('A', 'B'), Edge('A', 'C'),
        Edge('B', 'D'), Edge('B', 'E'),
        Edge('C', 'F'), Edge('C', 'G'),
        Edge('D', 'H'), Edge('D', 'I'),
        Edge('A', 'J'), Edge('A', 'K'),
        Edge('B', 'L'), Edge('C', 'M'),
        Edge('H', 'E')
    ]
    adjRep = AdjacencyRepresenter()
    adjacency_list = adjRep.from_edge_list(edge_list=edge_list)
    vertices = get_all_vertices(adj_list=adjacency_list)

    bfs = BFS(num_vertices=len(vertices), adjacency_list=adjacency_list)
    bfs.bfs('A')

    def print_path(path, only_new=True):
        vertices_visited = []
        for p in path:
            if only_new:
                if p[1] == 'visited':
                    continue
            vertices_visited.append(str(p[0]))
        return " -> ".join(vertices_visited)

    print(print_path(path=bfs.path_traversed))

    print(bfs.parents)

    net = create_pyvis_network(adjacency_list=adjacency_list)

    net.show('nodes.html')