class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        n = len(heights)

        for i in range(n):
            min_h = heights[i]

            for j in range(i, n):
                min_h = min(min_h, heights[j])
                area = min_h * (j - i + 1)
                max_area = max(max_area, area)

        return max_area

heights = list(map(int, input("Enter histogram heights separated by spaces: ").split()))

obj = Solution()
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))