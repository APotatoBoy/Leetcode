# encoding = utf-8

from sys import maxsize
class Solution:
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.
        :param x:int
        :return:int
        """
        lis = []
        i = 0
        res = 0
        tmp = abs(x)
        while tmp > 1 or tmp == 1:
            lis.append(tmp % 10)
            tmp = (int)(tmp / 10)
            i += 1
        for j in range(len(lis) - 1, -1, -1):
            res += lis[j] * pow(10, len(lis) - 1 - j)

        if res > maxsize or res < -1 * maxsize - 1:
            return 0

        if x > 0:
            return res
        elif x < 0:
            return res * -1
        else:
            return 0



x = 12345
sol = Solution()
y = sol.reverse(x)
print(y)

