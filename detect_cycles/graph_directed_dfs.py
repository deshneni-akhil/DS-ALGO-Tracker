def detect_cycle_directed_dfs(graph, nodes):
    visited = set()
    rec_stack = set()
    # Returns True if cycle is detected
    def dfs(node):
        if node in rec_stack:
            return True 
        if node in visited:
            return False
        rec_stack.add(node)
        for neighbour in graph.get(node, []):
            if dfs(neighbour):
                return True
        visited.add(node)
        rec_stack.remove(node)
        return False
    # Check for cycle in each node
    for node in range(nodes):
        if node not in visited and dfs(node):
            return True 
    return False

graph = {
    0: [1, 2],
    1: [2],
    2: []
}

print(detect_cycle_directed_dfs(graph, len(graph))) # True