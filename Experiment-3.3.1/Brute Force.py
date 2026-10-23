
def validPath(n, edges, source, destination):
    if source == destination:
        return True

    visited = set()

    def dfs(node):
        visited.add(node)

        if node == destination:
            return True

        for u, v in edges:
            if u == node and v not in visited:
                if dfs(v):
                    return True

            elif v == node and u not in visited:
                if dfs(u):
                    return True

        return False

    return dfs(source)


# Taking user input
n = int(input("Enter number of vertices: "))

m = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v):")
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

source = int(input("Enter source: "))
destination = int(input("Enter destination: "))

# Display result
if validPath(n, edges, source, destination):
    print("True")
else:
    print("False")
