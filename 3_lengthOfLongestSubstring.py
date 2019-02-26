#encoding=utf-8
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.
        :param s:
        :return:longest substring
        """
        mark = set([])
        length = len(s)
        j = 0
        maxLength = 0
        for i in range(length):
            while j < length and s[j] not in mark:
                mark.add(s[j])
                j += 1
            maxLength = max(maxLength, j - i)
            mark.remove(s[i])
        return maxLength


s = "auba"
sol = Solution().lengthOfLongestSubstring(s)
print(sol)
