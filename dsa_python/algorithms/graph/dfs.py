from typing import Dict, List, Any

from dsa_python.data_structures.graphs.adjacency_list import (
    AdjacencyRepresenter, Edge, get_all_vertices, create_pyvis_network
)


def calc_num_vertices(adj_list):
    vertices = set()
    for k, v in adj_list.items():
        vertices.add(k)
        for adj_node in v:
            vertices.add(adj_node)
    return len(vertices)


class DFS:
    def __init__(self, num_vertices, adjacency_list: Dict) -> None:
        self.N = num_vertices
        self.adj_list = adjacency_list
        self.visited = set()
        self.parents = {}
        self.cycle_node = None
        self.path_traversed = []

    def dfs(self, vertex):
        if vertex in self.visited:
            self.path_traversed.append((vertex, 'visited'))
            return

        self.path_traversed.append((vertex, 'new'))
        self.visited.add(vertex)  # Mark the vertex as traversed

        adj_vertices = self.adj_list.get(vertex)
        for next_vertex in adj_vertices:
            self.parents[next_vertex] = vertex
            self.dfs(next_vertex)

    def dfs_recursive_with_cycle_finding(self, vertex, parent):
        self.visited[vertex] = True  # Mark the vertex as traversed
        adj_vertices = self.adj_list.get(vertex)
        for next_vertex in adj_vertices:
            if not self.visited[next_vertex]:
                self.parents[next_vertex] = vertex
                self.dfs_recursive(next_vertex, vertex)
            else:
                if next_vertex != parent and self.cycle_node is None:
                    self.parents[next_vertex] = vertex
                    self.cycle_node = next_vertex
        return

    def do_depth_first_search(self, adjacency_rep: AdjacencyRepresenter):
        all_vertices = adjacency_rep.all_vertices
        start_node = all_vertices[0]
        self.dfs(start_node)


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
    n_vertices = len(vertices)

    dfs = DFS(num_vertices=n_vertices, adjacency_list=adjacency_list)
    dfs.dfs('A')

    def print_path(path, only_new=True):
        vertices_visited = []
        for p in path:
            if only_new:
                if p[1] == 'visited':
                    continue
            vertices_visited.append(str(p[0]))
        return " -> ".join(vertices_visited)

    print(print_path(path=dfs.path_traversed))

    net = create_pyvis_network(adjacency_list=adjacency_list)

    net.show('nodes.html')
