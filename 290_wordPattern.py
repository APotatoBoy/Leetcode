class Solution:
    def wordPattern(self, pattern, str):
        lis_str = str.split(' ')
        if len(pattern) != len(lis_str):
            return False
        dict = {}
        for i in range(0, len(pattern)):
            if pattern[i] in dict:
                if dict[pattern[i]] != lis_str[i]:
                    return False
            else:
                dict[pattern[i]] = lis_str[i]

        return len(dict.values()) == len(set(dict.values()))
pattern = 'abba'
str = 'dog dog dog dog'
print(Solution().wordPattern(pattern, str))