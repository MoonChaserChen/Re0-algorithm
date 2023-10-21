class UnionFind:
    def __init__(self, n: int):
        self.roots = [i for i in range(n)]
        # root值为当前树的节点数；非root值为1(其实没有意义)
        self.sizes = [1] * n

    def find(self, x: int) -> int:
        if self.roots[x] == x:
            return x
        else:
            self.roots[x] = self.find(self.roots[x])
            return self.roots[x]

    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.sizes[rx] > self.sizes[ry]:
                self.roots[ry] = rx
                self.sizes[rx] += self.sizes[ry]
            else:
                self.roots[rx] = ry
                self.sizes[ry] += self.sizes[rx]

    def getSize(self, x: int) -> int:
        return self.sizes[x]