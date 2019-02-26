class Solution:
    def missingNumber(self, nums):
        sum = 0
        max = nums[0]
        min = nums[0]
        for i in nums:
            sum += i
            if i > max:
                max = i
            if i < min:
                min = i
        if min != 0:
            return 0
        res = int(max * (max - min + 1) / 2) - sum
        if res == 0:
            return max + 1

        else:
            #res = int(max * (len(nums) + 1) / 2) - sum
            return res

nums = [1,0,2]
print(Solution().missingNumber(nums))