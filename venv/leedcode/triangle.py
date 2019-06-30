from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mini = triangle[len(triangle) - 1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                mini[j] = triangle[i][j] + min(mini[j], mini[j + 1])
        return mini[0]


def run():
    v = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    ret = Solution().minimumTotal(v)
    print("ret = ", ret)
