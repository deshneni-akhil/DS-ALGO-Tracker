from linkedlist_helper import LinkedList
import random, time
from typing import Optional
from collections import deque
from reverse_list import reverse_iterative

def approach_1(head: Optional[LinkedList], ll: Optional[LinkedList]) -> None:
    # time complexity is O(N (length of list) + (N/2*N) for getting first and last) overall O(N^2)
    # space complexity is O(N for creating a new list) overall O(N)

    def transform_input(main, copy):
        curr_main = main
        curr_copy = copy
        while curr_copy:
            curr_main.data = curr_copy.data
            curr_main = curr_main.next
            curr_copy = curr_copy.next

    def get_length(head: Optional[LinkedList]) -> int:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def get_nth_node(head: Optional[LinkedList], idx: int) -> int:
        # print('head I got', head.data,' and to retrive ',idx,' element')
        count = 0
        curr = head
        while curr:
            if count == idx:
                return curr
            count += 1
            curr = curr.next
        return None

    n = get_length(head)
    # print(n)
    half = n // 2
    reorder = LinkedList(-1)
    curr = reorder
    main = head
    for i in range(half):
        first = main
        last = get_nth_node(head, n-i-1)
        # print(first.data,'->',last.data)
        curr.next = LinkedList(first.data)
        curr = curr.next
        curr.next = LinkedList(last.data)
        curr = curr.next
        main = main.next
    
    if n & 1:
        # If n is odd then add the middle node at the end
        last_node = get_nth_node(head, half)
        curr.next = LinkedList(last_node.data)
    
    # self.printer(reorder.next)
    transform_input(head, reorder.next)

def approach_2(head: Optional[LinkedList], ll: Optional[LinkedList]) -> None:
    # the time complexity is O(N) and space complexity is O(N)
    n = ll._get_length()
    stack = deque()
    curr = head
    while curr:
        stack.appendleft(curr)
        curr = curr.next
    length = n
    prev = None
    while length > 1:
        first = stack.pop()
        last = stack.popleft()
        if prev:
            # prev pointer is used to connect the last node of the previous pair to the first node of the current pair
            prev.next = first
        first.next = last 
        prev = last
        length -= 2
    if stack:
        prev.next = stack.pop()
        # setting the next of the last node to None
        prev.next.next = None
    else:
        # setting the next of the last node to None
        prev.next = None
    return 

def approach_3(head: Optional[LinkedList], ll: Optional[LinkedList]) -> None:
    # The overall tc is O(N) and space complexity is O(1)
    # getting the middle of node the time complexity is O(N)
    middle_node = ll._get_middle()
    # reversing the nodes the time complexity is O(N/2)
    reverse = reverse_iterative(middle_node)
    # rest of the algorithm
    curr_last = reverse
    curr_first = head
    prev = None
    while curr_last:
        if curr_last == curr_first:
            # If the length is odd then both will hold the same references at the end of loop
            break
        temp = curr_first.next 
        if prev:
            # this is to link the last element of previous pair to the current first node
            prev.next = curr_first
        curr_first.next = curr_last 
        prev = curr_last
        curr_last = curr_last.next
        curr_first = temp
    if curr_last:
        # If the length is odd then add the middle node at the end of the list
        prev.next = curr_last

def approach_4(head: Optional[LinkedList], ll: Optional[LinkedList]) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    
    second = slow.next 
    prev = second.next = None 
    while second:
        tmp = second.next 
        second.next = prev 
        prev = second 
        second = tmp 
    
    first, second = head, prev 
    while second:
        temp1, temp2 = first.next, second.next 
        first.next = second
        second.next = temp1 
        first, second = temp1, temp2 

def reorderList(head: LinkedList, ll: Optional[LinkedList], function: object) -> None:
    return function(head, ll)

if __name__ == '__main__':
   
    ll = LinkedList()
    nums = [i for i in range(1, random.randint(int(10),int(1e2)))]
    solutions = [approach_1, approach_2, approach_3, approach_4]
    
    head = ll.get_linked_list(nums)
    solution = random.choice(solutions)
    
    start = time.time()
    reorderList(head, ll, solution)
    end = time.time()

    print(f'Solution: {solution.__name__}')
    print(f'Input size: {len(nums)} elements')
    print(f'Execution time: {(end-start):.4f} seconds')
    ll.__str__()

'''
Test results:

Size of the input is 9999 elements
-----------------------------------
Solution: approach_1
Input size: 9999 elements
Execution time: 1.3015 seconds

Solution: approach_2
Input size: 9999 elements
Execution time: 0.0010 seconds

Solution: approach_3
Input size: 9999 elements
Execution time: 0.0010 seconds
-----------------------------------

Size of the input is 99999 elements

Solution: approach_3
Input size: 99999 elements
Execution time: 0.0050 seconds

Solution: approach_2
Input size: 99999 elements
Execution time: 0.0081 seconds

Solution: approach_1
Input size: 99999 elements
Execution time: 195.9454 seconds
'''