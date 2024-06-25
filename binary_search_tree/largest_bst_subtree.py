from tree_templates.tree_builder import BuildTree as BT 
from typing import Tuple

def isBST(root:'BT',min_left:int,max_right:int) -> Tuple[bool,int]:
    if not root:
        return (True,0)
    if root.val <= min_left or root.val >= max_right:
        return (False,1)
    left_is_bst, l_count = isBST(root.left, min_left ,root.val)
    right_is_bst, r_count = isBST(root.right, root.val, max_right)
    if left_is_bst and right_is_bst:
        return (True, l_count+r_count+1)
    return (False, max(l_count,r_count))

def helper(root:'BT', min_value:int, max_value:int) -> int:
    if not root:
        return 0
    is_bst, size = isBST(root, min_value, max_value)
    left = right = 0
    if is_bst:
        return size
    else:
        left = helper(root.left, min_value, max_value)
        right = helper(root.right, min_value, max_value)
    return max(left,right)

if __name__ == '__main__':
    root = BT()
    arr = [4,2,7,2,3,5,None,2,None,None,None,None,None,1]
    root = root.level_order_insert(arr)
    print(f'Max bst subtree in the given tree is at length {helper(root,float("-inf"),float("inf"))}')



