class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1 :
            return x
        m = 0
        l = 1
        r = x
        res = 0
        while l <= r :
            m = int (r - (r - l) / 2)
            if m == int (x / m) :
                return  m
            elif m > int (x / m) :
                r = m - 1
            else :
                l = m + 1
                res = m

        return int(res)



def run() :
    s = Solution()
    print("ret = ", s.mySqrt(4))