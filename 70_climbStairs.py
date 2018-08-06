# encoding = utf-8


class Solution:
    def climbStairs(self, n):
        """
        Each time you can either climb 1 or 2 steps. In how many distinct ways to the top
        :param n: int
        :return: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        res = [1, 2]
        for i in range(n - 2):
            res.append(res[-1] + res[-2])
        return res[-1]
        #return Solution().climbStairs(n -1) + Solution().climbStairs(n - 2)


n = 3
res = Solution().climbStairs(n)
print(res)