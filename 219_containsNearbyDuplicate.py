class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for index, element in enumerate(nums):
            if element in dict:
                distance = index - dict[element]
                if distance <= k:
                    return True
                dict[element] = index
            else:
                dict[element] = index
        return False

nums = [1, 0, 1, 1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))
