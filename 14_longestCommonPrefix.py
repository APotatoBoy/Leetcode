# encoding = uft-8

class Solution:
    def longestCommonPrefix(self, strs):
        """
        Find the longest common prefix string amongst an array of strings
        :param strs:List[str]
        :return:str
        """
        length = len(strs)
        if length == 0:
            return ""
        elif length == 1:
            return strs[0]
        else:
            shortestLength = Solution().getShortestLength(strs)
            #print(shortestLength)
            currentLength = 1
            while currentLength < shortestLength + 1:
                for i in range(0, len(strs)):
                    if (strs[0])[:currentLength] != strs[i][:currentLength]:
                        return (strs[0])[:currentLength -1]
                currentLength += 1
            #print(currentLength)
            return (strs[0])[:currentLength - 1]


    def getShortestLength(self, strs):
        if len(strs) == 0:
            return -1

        minLength = len(strs[0])
        for i in range(len(strs)):
            if minLength > len(strs[i]):
                minLength = len(strs[i])
        return minLength


strs = ["flower","flow","flight"]
sCommon = Solution().longestCommonPrefix(strs)
print(sCommon)