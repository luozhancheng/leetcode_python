
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res


def run():
    l = [2,3,-2,4]
    ret = Solution().maxProduct(l)
    print("ret = ", ret)

    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'],
              ['mike', '1999-01-01', 'male'],
              ['nancy', '2001-02-01', 'female']
              ]

    out = [{attributes[j]:values[i][j] for j in range(len(attributes))} for i in range(0, len(values))]

    print(out)

    # expected outout:
    [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
     {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
     {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

