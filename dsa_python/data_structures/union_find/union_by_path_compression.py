"""
    Union by Path Compression implementation of Union Find
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

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
