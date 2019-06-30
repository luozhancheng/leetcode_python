from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        vec: List[int] = []

        for i in range(0, len(nums)):
            index = self.lowerBound(vec, 0, len(vec) - 1, nums[i])
            if index == -1:
                vec.append(nums[i])
            else:
                vec[index] = nums[i]

        return len(vec)

    def lowerBound(self, vec: List[int], begin: int, end: int, val: int) -> int:
        if len(vec) == 0:
            return -1
        if begin >= len(vec) or begin > end:
            return -1

        index: int = int(begin + (end - begin) / 2)
        if vec[index] >= val:
            if begin == end:
                return index
            return self.lowerBound(vec, 0, index, val)
        else:
            return self.lowerBound(vec, index + 1, end, val)
        return index


def run():
    vec = [10, 9, 2, 5, 3, 7, 101, 18]

    ret = Solution().lengthOfLIS(vec)
    print("ret = ", ret)
