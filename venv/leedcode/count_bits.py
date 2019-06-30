from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0] * (num + 1)
        for i in range(1, num + 1):
            ret[i] = ret[i & (i - 1)] + 1
        return ret





def run():
    s = Solution()
    ret = s.countBits(5)
    for i in ret:
        print(i, " ")
