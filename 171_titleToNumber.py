#encoding = utf-8
class Solution:
    def titleToNumber(self, s):
        """
        Given a column title as appear in an Excel sheet, return its corresponding column number.
        :param s:
        :return:column number
        """
        number = 0
        length = len(s)
        if length == 0:
            return 0
        else:
            times = 0
            for i in range(length - 1, -1, -1):
                number += (ord(s[i]) - 64) * pow(26, times)
                times += 1
        return number

s = "ZY"
sol = Solution().titleToNumber(s)
print(sol)
