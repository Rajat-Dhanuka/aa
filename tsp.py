#implement DP strategy to solve the Traveling Salesman Problem (TSP).
import sys

def tsp_dp(graph):
    n = len(graph)
    # Initialize the DP table with all nodes and no edges visited
    dp = [[None] * (1 << n) for _ in range(n)]
    start = 0  # Start from the first city

    # Helper function to recursively find the shortest path
    def dfs(node, visited):
        # Base case: If all cities are visited, return the distance to start city
        if visited == (1 << n) - 1:
            return graph[node][start]
        # If already computed, return the result
        if dp[node][visited] is not None:
            return dp[node][visited]

        # Initialize the minimum distance to infinity
        min_dist = sys.maxsize
        for next_node in range(n):
            # If next_node is not visited yet
            if (visited & (1 << next_node)) == 0:
                # Calculate the distance to next_node and add it to the total distance
                dist = graph[node][next_node] + dfs(next_node, visited | (1 << next_node))
                # Update the minimum distance
                min_dist = min(min_dist, dist)

        # Memoize the result
        dp[node][visited] = min_dist
        return min_dist

    # Start the recursive search from the start node
    return dfs(start, 1 << start)

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Shortest path length:", tsp_dp(graph))