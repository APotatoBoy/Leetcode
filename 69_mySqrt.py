# encoding = utf-8
import math

class Solution:
    def mySqrt(self, x):
        """
        Return the int square of root of x
        :param x:int
        :return:int
        """
        if x < 0:
            return -1
        if x == 1:
            return 1
        start = 0
        end = x
        middle = 0
        while start < end - 1:
            middle = math.ceil((start + end) / 2)
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                end = middle
            else:
                start = middle
        return min(start, end)


x = 15
res = Solution().mySqrt(x)
print(res)
