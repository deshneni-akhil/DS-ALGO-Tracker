from tree_builder import BuildTree as BT

def morris_inorder_traversal(root) -> list[int]:
    # Morris Traversal is a way to traverse the tree without using the stack and recursion.
    # It uses the threaded binary tree to traverse the tree.
    # The algorithm takes O(n) time and O(1) space.
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                res.append(curr.val)
                curr = curr.right
    print(res)
    return res
    
if __name__ == '__main__':
    arr = [1, 2, 3, None, None, 6, 7]
    tree = BT()
    root = tree.level_order_insert(arr)
    morris_inorder_traversal(root)
