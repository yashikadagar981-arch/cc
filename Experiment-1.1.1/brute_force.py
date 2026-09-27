class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False