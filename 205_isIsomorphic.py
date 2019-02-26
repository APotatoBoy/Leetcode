class Solution:
    def isIsomorphic(self, s, t):
        """
        判断两个字符串是否同构
        :param s: str
        :param t: str
        :return: bool
        """
        dict = {}
        #构建初始映射表
        for i in range(0, 128):
            dict[chr(i)] = chr(i)
        #字符映射
        for i in range(0, len(s)):
            if s[i] == t[i]:
                continue
            else:
                dict[s[i]] = t[i]
        bo = [0] * 127
        # s中所有出现的字符
        str_in_s = ''
        for i in s:
            if i in str_in_s:
                continue
            else:
                str_in_s += i
        # 判断是否有多个字符映射为同一个字符的情况
        for key in str_in_s:
            if bo[ord(dict[key])] == 0:
                bo[ord(dict[key])] = 1
            else:
                return False
        for i in range(0, len(s)):
            if dict[s[i]] != t[i]:
                return False
        return True

s = 'egg'
t = 'add'
print(Solution().isIsomorphic(s, t))

