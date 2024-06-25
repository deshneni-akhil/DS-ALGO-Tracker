from collections import deque

class BuildTree:

    # Constructor to initialize the left, right and val of the node
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    # Level order insertion will occur where the elements will be inserted in Complete Binary Tree way.
    def level_order_insert(self,values:list[int]) -> 'BuildTree':
        if not values:
            raise ValueError("Values are not provided")
        self.root = BuildTree()
        self.root.val = values[0]
        index = 1
        queue = deque()
        queue.append(self.root)
        while queue:
            length = len(queue)
            while length:
                node = queue.popleft()
                if index < len(values):
                    if values[index]:
                        node.left = BuildTree()
                        node.left.val = values[index]
                        queue.append(node.left)
                    index += 1
                if index < len(values):
                    if values[index]:
                        node.right = BuildTree()
                        node.right.val = values[index]
                        queue.append(node.right)
                    index += 1
                length -= 1
        return self.root


# Testing the code to check the implementation
if __name__ == "__main__":
    tree = BuildTree()
    root = tree.level_order_insert([1,2,3,None,None,6,7])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.left.val)
    print(root.right.right.val)


