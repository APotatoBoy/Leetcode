# encoding = utf-8
import math
class Solution:
    def searchInsert(self, nums, target):
        """
        return the index where to insert the given target
        :param nums:List[int]
        :param target:int
        :return:int
        """
        length = len(nums)
        middle = (int) (length / 2)
        while middle > 0 and middle < length:
            if nums[middle] < target:
                middle = math.ceil((length + middle) / 2)
            elif nums[middle] > target:
                middle = math.floor(middle / 2)
            else:
                return middle
        if middle == 0:
            if target > nums[middle]:
                return middle + 1
            else:
                return middle
        elif middle == length:
            if target > nums[middle - 1]:
                return middle + 1
            else:
                return middle
        return middle



nums = [1,3,5]
target = 4
index = Solution().searchInsert(nums, target)
print(index)