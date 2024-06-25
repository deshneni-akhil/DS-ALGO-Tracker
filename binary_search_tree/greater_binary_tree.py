# Question is from LeetCode #538
# Problem: Convert BST to Greater Tree
from tree_templates.tree_builder import BuildTree as BT
from binary_tree.traversals import level_order_traversal
bst_sum = 0

def bstToGst(root:'BT',carry: int) -> 'BT':
    if not root:
        return carry
    carry = bstToGst(root.right, carry)
    carry += root.val
    root.val = carry
    carry = bstToGst(root.left, carry)
    return carry

if __name__ == '__main__':
    root = BT()
    arr = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root = root.level_order_insert(arr)
    # level_order_traversal(root)
    ans = bstToGst(root, 0)
    level_order_traversal(root)