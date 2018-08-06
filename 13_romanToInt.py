# encoding = uft-8

class Solution:
    def romanToInt(self, s):
        """
        Change a roman numerals to an integer
        :param s:string
        :return:int
        """
        dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500:"D", 1000: "M"}
        key_dict = list(dict.keys())
        value_dict = list(dict.values())
        lis = []
        res = 0
        for i in range(len(s)):
            lis.append(s[i])
        #print(lis)
        j = 0
        while j < len(lis):
            if j < len(lis) - 1:
                if key_dict[value_dict.index(lis[j])] < key_dict[value_dict.index(lis[j + 1])]:
                    if lis[j] == "I":
                        if lis[j + 1] == "V":
                            temp = 4
                        elif lis[j + 1] == "X":
                            temp = 9
                    if lis[j] == "X":
                        if lis[j + 1] == "L":
                            temp = 40
                        elif lis[j + 1] == "C":
                            temp = 90
                    if lis[j] == "C":
                        if lis[j + 1] == "D":
                            temp = 400
                        elif lis[j + 1] == "M":
                            temp = 900
                    j += 2
                else:
                    temp = key_dict[value_dict.index(lis[j])]
                    j += 1
            else:
                temp = key_dict[value_dict.index(lis[j])]
                j += 1
            #print(temp)
            res += temp
        return res


s = "DCXXI"
sol = Solution()
y = sol.romanToInt(s)
print(y)