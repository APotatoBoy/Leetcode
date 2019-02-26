class Solution:

    def isHappy(self, n):
        """
        快乐数
        :param n: int
        :return: bool
        """
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x)*int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1


n = 19
ret = Solution().isHappy(n)
print(ret)