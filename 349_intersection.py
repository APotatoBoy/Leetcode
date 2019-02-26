class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

nums1 = [1,2,3,4,1,4]
nums2 = [1,3,4,7,2]
print(Solution().intersection(nums1, nums2))