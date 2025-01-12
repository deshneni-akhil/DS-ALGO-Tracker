from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class GraphClone:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        
        if not node:
            return node

        def cloner(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(cloner(neighbor))
            return copy
            
        cloner(node)
        return clone[node]

    def print_graph(self, node, visited):
        if not node or node in visited:
            return
        print(node.val)
        visited.add(node)
        for neighbor in node.neighbors:
            self.print_graph(neighbor, visited)

# Test
node = Node(1)
node2 = Node(2)
node3 = Node(3)
node.neighbors = [node2]
node2.neighbors = [node2, node3]
node3.neighbors = [node2]

graph = GraphClone()
result = graph.cloneGraph(node) 
graph.print_graph(result, set())

