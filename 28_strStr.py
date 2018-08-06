# encoding = utf-8

class Solution:
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack
        :param haystack:str
        :param needle:str
        :return:int
        """
        if needle == "":
            return 0
        index = haystack.find(needle)
        return index


haystack = "aaaaa"
needle = "bba"
index = Solution().strStr(haystack, needle)
print(index)