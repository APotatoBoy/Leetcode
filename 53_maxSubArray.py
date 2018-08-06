# encoding = utf-8

import sys
class Solution:
    def maxSubArray(self, nums):
        """
        find the contiguous subarray which has the largest sum
        :param nums:
        :return:
        """
        if nums is None or len(nums) == 0:
            return 0
        maxSum = -sys.maxsize - 1#keep max sum of nums
        curSum = 0 #keep current max
        for i in range(len(nums)):
            if curSum <= 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            if maxSum < curSum:
                maxSum = curSum

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = Solution().maxSubArray(nums)
print(maxSum)