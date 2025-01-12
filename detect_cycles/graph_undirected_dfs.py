# this code works but sucks at time complexity reaching time complexity of O(V + E) ^ 2
def undirected_dfs_slow(graph):
    visited = set()

    def dfs(node, parent):
        if node in visited and node != parent:
            return True 
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour != parent and dfs(neighbour, node):
                return True 
        visited.remove(node)
        return False 
    
    for node in range(len(graph)):
        if dfs(node, -1):
            return True 
    return False

# time complexity of this logic is O(V+E)
def undirected_dfs_optimized(graph, V):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbour in graph[node]:
            if (neighbour not in visited):
                if (dfs(neighbour, node)):
                    return True
            elif neighbour != parent:
                return True 
        return False 
    for node in range(V):
        if node not in visited and dfs(node, -1):
            return True 
    return False

def undirected_dfs_graph_coloring(graph, V):
    class Colors:
        grey = 0
        black = 1
        red = 2
    states = [Colors.grey] * V
    pass # need to implement this

# graph with cycle
# graph = {
#     0: [1],
#     1: [0, 2, 4],
#     2: [1, 3],
#     3: [2, 4],
#     4: [1, 3]
# }

# graph without cycle 
graph = {
    0: [],
    1: [2],
    2: [1, 3],
    3: [2]
}

# res = undirected_dfs(graph)
res = undirected_dfs_optimized(graph, len(graph))
statement = 'cycle detected' if res else 'no cycle detected'
print(statement)