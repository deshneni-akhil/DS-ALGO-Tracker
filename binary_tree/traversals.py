from tree_templates.tree_builder import BuildTree as BT
from collections import deque

def recursive_inorder(root:'BT') -> None:
    if not root:
        return
    recursive_inorder(root.left)
    print(root.val,end=" ")
    recursive_inorder(root.right)

def iterative_inorder(root:'BT') -> None:
    if not root:
        return
    queue = []
    curr = root
    while queue or curr:
        while curr:
            queue.append(curr)
            curr = curr.left
        curr = queue.pop()
        print(curr.val,end=" ")
        curr = curr.right

def recursive_preorder(root:'BT') -> None:
    if not root:
        return
    print(root.val,end=" ")
    recursive_preorder(root.left)
    recursive_inorder(root.right)

def iterative_preorder(root:'BT') -> None:
    if not root:
        return
    queue = []
    curr = root 
    while queue or curr:
        while curr:
            print(curr.val,end=' ')
            queue.append(curr)
            curr = curr.left
        curr = queue.pop()
        curr = curr.right

def recursive_postorder(root:'BT') -> None:
    if not root:
        return 
    recursive_postorder(root.left)
    recursive_postorder(root.right)
    print(root.val,end=" ")

def iterative_postorder(root:'BT') -> None:
    if not root:
        return 
    queue, curr = [] , root
    pre = None
    while curr or queue:
        while curr:
            queue.append(curr)
            curr = curr.left 
        else:
            curr = queue[-1]
            if not curr.right or curr.right == pre:
                print(curr.val,end=' ')
                queue.pop()
                pre = curr 
                curr = None
            else:
                curr = curr.right

def level_order_traversal(root:'BT') -> None:
    queue = deque()
    queue.append(root)
    buffer = []
    while queue:
        length = len(queue)
        while length > 0:
            curr = queue.popleft()
            buffer.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            length -= 1
        print(*buffer)
        buffer = list()
    
if __name__ == '__main__':
    tree = BT()
    arr = [1,None,2,3]
    root = tree.level_order_insert(arr)
    # recursive_inorder(root)
    # print()
    # iterative_inorder(root)
    # recursive_preorder(root)
    # print()
    # recursive_inorder(root)
    # recursive_postorder(root)
    # print()
    # iterative_postorder(root)
    level_order_traversal(root)
