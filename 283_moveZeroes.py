class Solution:
    def moveZeroes(self, nums):
        num_of_zero = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                num_of_zero += 1
            elif num_of_zero > 0:
                nums[i-num_of_zero] = nums[i]
            else:
                continue
        for j in range(0, num_of_zero):
            nums[len(nums) - 1 - j] = 0
        #return nums

nums = [0,1,0,0,3,12, 0, 0]
Solution().moveZeroes(nums)
print(nums)
