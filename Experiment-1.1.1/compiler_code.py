def containsNearbyDuplicate(nums, k):
    num_indices = {}
    for current_index, current_num in enumerate(nums):
        if current_num in num_indices:
            if current_index - num_indices[current_num] <= k:
                return True
        num_indices[current_num] = current_index
    return False
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
k = int(input("Enter value of k: "))
result = containsNearbyDuplicate(nums, k)
print(result)