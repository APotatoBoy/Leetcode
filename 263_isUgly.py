class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        while not num % 2:
            num = int(num/2)
        while not num % 3:
            num = int(num/3)
        while not num % 5:
            num = int(num/5)
        return num == 1

num = 6
print(Solution().isUgly(num))