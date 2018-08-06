# encoding = utf-8

class Solution:
    def removeDuplicates(self, nums):
        """
        Remove the duplicates in-place such that each element appear only once and return
        the new length
        :param nums: List[int]
        :return: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                #i -= 1
            else:
                i += 1
        #print(nums)
        return len(nums)

nums = [0,0,1,1,1,2,2,2,3,3,4]
length = Solution().removeDuplicates(nums)
print(length)
print(nums)

