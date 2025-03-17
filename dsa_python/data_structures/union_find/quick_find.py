"""
    Quick Find implementation of Union Find
    
    Quick Find because instead of storing parents, we are storing root nodes.
    
    Quick Union would focus on storing parents, but find operation would become slower 
    as we would traverse the parents array until we find the roots.
"""


class UnionFind:
    def __init__(self, size):
        self.root = [0] * size
        for i in range(size):
            self.root[i] = i

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

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
