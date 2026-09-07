class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result

candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

obj = Solution()
result = obj.combinationSum(candidates, target)

print("Combinations:")
print(result)