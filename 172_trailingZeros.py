#encoding=utf-8

class Solution:
    def trailingZeroes(self, n):
        """
        calculate the number of factors 5 from 0 to n
        :param n:
        :return:number of zeros
        """
        if n < 5:
            return 0
        while (n % 5 != 0):
            n -= 1
        return int(n / 5 + Solution().trailingZeroes(n / 5))

n = 50
sol = Solution().trailingZeroes(n)
print(sol)
