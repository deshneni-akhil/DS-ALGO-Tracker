from tree_templates.tree_builder import BuildTree as BT
import random

def twoSumBSTs(root1: 'BT', root2: 'BT', target: int) -> bool:

        def binary_search(root, search):
            if not root:
                return False
            if root.val == search:
                return True
            L = R = False
            if root.val >= search:
                L = binary_search(root.left,search)
            else:
                R = binary_search(root.right,search)
            return L or R

        def traverse(root1,root2,target):
            if not root1:
                return False
            if binary_search(root2,target-root1.val):
                return True
            return traverse(root1.left,root2,target) or traverse(root1.right,root2,target)

        return traverse(root1,root2,target)

if __name__ == '__main__':
    tree = BT()
    arr1 = [0,-10,10]
    arr2 = [5,1,7,0,2] 
    root1 = tree.level_order_insert(arr1)
    root2 = tree.level_order_insert(arr2)
    target = random.randint(0,10)
    print(twoSumBSTs(root1,root2,target))