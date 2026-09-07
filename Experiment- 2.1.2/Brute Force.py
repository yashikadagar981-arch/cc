class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def generate(current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for num in candidates:
                current.append(num)
                generate(current, total + num)
                current.pop()

        generate([], 0)

        unique = []

        for combination in result:
            combination.sort()

            if combination not in unique:
                unique.append(combination)

        return unique

candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

obj = Solution()
result = obj.combinationSum(candidates, target)

print("Combinations:")
print(result)