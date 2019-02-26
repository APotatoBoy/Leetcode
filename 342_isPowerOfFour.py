class Solution:
    def isPowerOfFour(self, num):
        if num < 0 or (num & (num -1)):
            return False
        return not num & 0x55555555 == 0

num = 5
print(Solution().isPowerOfFour(num))