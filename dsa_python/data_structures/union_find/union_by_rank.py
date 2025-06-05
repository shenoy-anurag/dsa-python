"""
    Union by Rank implementation of Union Find
    
    Union by Rank so that we can balance the tree.
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

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
