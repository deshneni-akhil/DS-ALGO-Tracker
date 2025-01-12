from collections import deque

def toplogical_sort_cycle(graph):
    in_degree = [0] * len(graph)
    for node in graph:
        for neighbour in graph[node]:
            in_degree[neighbour] += 1
    
    q = deque()
    q.extend([node for node in range(len(graph)) if in_degree[node] == 0])
    topo_order = []
    while q:
        curr_node = q.popleft()
        print(curr_node)
        topo_order.append(curr_node)
        for neighbour in graph[curr_node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                q.append(neighbour)
    if len(topo_order) != len(graph):
        print('Cycle detected')
    else:
        print('No cycle detected')

graph = {
    0: [1, 2],
    1: [2],
    2: [0]
}
