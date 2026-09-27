class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        return result

nums = list(map(int, input("Enter elements: ").split()))
obj = Solution()

result = obj.subsets(nums)
print("All subsets:")
for subset in result:
    print(subset)