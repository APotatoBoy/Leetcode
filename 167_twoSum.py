# encoding = utf-8

class Solution:
    def twoSum(self, numbers, target):
        """
        find two numbers such that they add up to a specific target number
        :param numbers: List[int]
        :param target: int
        :return: List[int]
        """
        length = len(numbers)
        if length < 2:
            return []
        #for index1 in range(length):
        index1 = 0
        while index1 < length:
            temp = target - numbers[index1]
            index2 = index1 + 1
            #if numbers[index2] == numbers[index1] and index2 < length:
             #   index2 += 1
            if temp < 0:
                return []
            else:
                while index2 < length:
                    if numbers[index2] == temp:
                        return [index1+1, index2+1]
                    index2 += 1
            while numbers[index1 + 1] == numbers[index1] and index1 < length:
                index1 += 1
            index1 += 1

        return []


numbers = [0, 0, 0, 0, 1, 2, 2, 3]
target = 5
res = Solution().twoSum(numbers, target)
print(res)