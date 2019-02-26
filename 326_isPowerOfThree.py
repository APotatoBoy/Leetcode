class Solution:
    def isPowerOfThree(self, n):
        #整数范围内最大的3的幂方
        #3的所有幂方的质因子只有3，因此必能被最大的幂方整除
        return n > 0 and 1162261467 % n == 0

n = 27
print(Solution().isPowerOfThree(n))