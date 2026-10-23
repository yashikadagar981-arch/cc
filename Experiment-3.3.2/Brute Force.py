
def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(i, j):
        if (i < 0 or i >= rows or
            j < 0 or j >= cols or
            grid[i][j] == '0'):
            return

        grid[i][j] = '0'

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count


# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid elements (0 or 1):")
for i in range(rows):
    row = input().split()
    grid.append(row)

# Display Output
print("Number of Islands:", numIslands(grid))
