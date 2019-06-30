from typing import List


class UnionFind:
    def __init__(self, grid: List[List[str]]):
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.count += 1
                    self.parent[i * n + j] = i * n + j

    def find(self, i) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                for d in direction:
                    dx, dy = i + d[0], j + d[1]
                    if dx >= 0 and dy >= 0 and dx < m and dy < n and grid[dx][dy] == "1":
                        uf.union(i * n + j, dx * n + dy)
        return uf.count


def run():
    grid2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    grid1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ret = Solution().numIslands(grid1)
    print("ret1 = ", ret)
    ret = Solution().numIslands(grid2)
    print("ret2 = ", ret)
    pass
