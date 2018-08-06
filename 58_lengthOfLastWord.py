# encodeing = utf-8

class Solution:
    def lengthOfLastWord(self, s):
        """
        return the last length of a str
        :param s:str
        :return:int
        """
        length = len(s)
        if length == 0 or s.isspace():
            return 0
        res = ''
        for i in range(-1, -1 * length - 1, -1):
            if (s[i].isalpha()):
                end = i
                while i > -1 * length - 1:
                    if s[i].isspace():
                        break
                    i -= 1
                return end - i
               # return s[i + length + 1:end + length + 1]

        return 0


s = "hello"
res = Solution().lengthOfLastWord(s)
print(res)