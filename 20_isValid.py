# encoding = utf-8

class Solution:
    def isValid(self, s):
        """
        Determine the input string is valid
        :param s:str
        :return:bool
        """
        if s == "":
            return True
        length = len(s);
        if length % 2 == 1:
            return False
        lis = []
        lookUp = {"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in lookUp:
                lis.append(i)
            elif len(lis) == 0 or lookUp[lis.pop()] != i:
                return False
        return len(lis) == 0


s = ""
res = Solution().isValid(s)
print(res)