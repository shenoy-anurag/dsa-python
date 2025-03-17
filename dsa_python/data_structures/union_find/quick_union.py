"""
    Quick Union implementation of Union Find
    
    Quick Union because instead of storing root, we are storing parent nodes.
    
    Quick Find would focus on storing root, but find operation would become faster.
"""


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]

    def find(self, x):
        while self.parents[x] != x:
            x = self.parents[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    uf = UnionFind(6)
    uf.union(1, 2)
    uf.union(2, 4)
    uf.union(2, 3)
    uf.union(0, 5)
    print(uf.connected(1, 4))
    print(uf.connected(1, 5))
    print(uf.connected(5, 0))
