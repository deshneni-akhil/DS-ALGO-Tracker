from linkedlist_helper import LinkedList

# Space timecomplexity is O(N) as it uses a recursion stack and uses O(N) space for time complexity
def reverse_recursive(head: LinkedList):
    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Time complexity is O(N) and space complexity is O(1) as it uses a few variables
def reverse_iterative(head: LinkedList):
    prev = nxt = None 
    curr = head 
    while curr:
        nxt = curr.next
        curr.next = prev 
        prev = curr
        curr = nxt 
    return prev

if __name__ == '__main__':
    nums = [i for i in range(1, 6)]
    linked_list = LinkedList()
    head = linked_list.get_linked_list(nums)
    linked_list.print_custom_list(head)
    # ans = reverse_recursive(head)
    ans = reverse_iterative(head)
    linked_list.print_custom_list(ans)