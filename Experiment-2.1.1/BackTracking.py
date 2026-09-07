class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result

nums = list(map(int, input("Enter elements: ").split()))
obj = Solution()
result = obj.subsets(nums)

print("All subsets:")
print(result)