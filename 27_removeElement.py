# encoding = utf-8

class Solution:
    def removeElement(self, nums, val):
        """
        Remove the given value from a list
        :param nums:
        :param val:
        :return:
        """
        i = 0
        while i < len(nums):
           if nums[i] == val:
               nums.pop(i)
           else:
               i += 1
        return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2
length = Solution().removeElement(nums, val)
print(nums)
print(length)

