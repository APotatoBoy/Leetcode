class Solution:
    def addDigits(self, num):
        s = str(num)
        while len(s) > 1:
            sum = 0
            for i in s:
                sum += int(i)
            s = str(sum)
        return int(s)

num = 38
print(Solution().addDigits(num))