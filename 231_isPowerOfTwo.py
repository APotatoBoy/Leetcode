class Solution:
    def decToBin(self, n):
        """
        10进制转二进制
        :param n: int
        :return: str
        """
        s_bin = ''
        while n > 0:
            ent = n % 2
            s_bin = str(ent) + s_bin
            n = n >> 1
        return s_bin

    def isPowerOfTwo(self, n):
        n_bin = self.decToBin(n)
        return n_bin == '1' + '0'*(len(n_bin) - 1)

n = 18
#print(Solution().decToBin(n))
print(Solution().isPowerOfTwo(n))