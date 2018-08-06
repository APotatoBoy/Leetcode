# encoding = utf-8

class Solution:
    def countAndSay(self, n):
        """
        the count-and-say sequence
        :param n:int
        :return:str
        """
        if n == 1:
            return '1'
        else:
            last = Solution().countAndSay(n - 1)
            lis = Solution().cutNum(last)
            #print(lis)
            res = ''
            for i in range(len(lis)):
                res += str(lis[i])
            #print(res)
            return res

    def cutNum(self, n):
        s = str(n)
        key = []
        value = []
        res = []
        num = 1
        i = 1
        diffNum = s[0]
        while i < len(s):
            if diffNum == s[i]:
                num += 1
            else:
                key.append(num)
                value.append(diffNum)
                diffNum = s[i]
                num = 1
            i += 1
        key.append(num)
        value.append(diffNum)
        for j in range(len(key)):
            res.append(str(key[j]))
            res.append(value[j])
        #print(res)
        return res


n = 4
y = Solution().countAndSay(n)
print(y)