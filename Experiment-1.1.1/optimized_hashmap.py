class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}
        for current_index, current_num in enumerate(nums):
            if current_num in num_indices:
                if current_index - num_indices[current_num] <= k:
                    return True
            num_indices[current_num] = current_index
        return False