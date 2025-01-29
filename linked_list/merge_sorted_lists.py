from linkedlist_helper import LinkedList
from typing import Optional

def approach_1(list1: Optional[LinkedList], list2: Optional[LinkedList]):
    # The time complexity is O(n + n + nlogn) = O(nlogn) and the space complexity is O(n)
    array = []
    while list1:
        array.append(list1.data)
        list1 = list1.next
    while list2:
        array.append(list2.data)
        list2 = list2.next
    array.sort()
    linkedlist = LinkedList()
    return linkedlist.get_linked_list(array)

def approach_2(list1: Optional[LinkedList], list2: Optional[LinkedList]):
    # The time complexity is O(n + n) = O(n) and the space complexity is O(n)
    array = []
    while list1 and list2:
        if list1.data <= list2.data:
            array.append(list1.data)
            list1 = list1.next
        else:
            array.append(list2.data)
            list2 = list2.next
    while list1:
        array.append(list1.data)
        list1 = list1.next 
    while list2:
        array.append(list2.data)
        list2 = list2.next 
    linkedlist = LinkedList()
    return linkedlist.get_linked_list(array)

def approach_3(list1: Optional[LinkedList], list2: Optional[LinkedList]):
    # time complexity is O(N) and space complexity is O(1)
    ll = LinkedList()
    head = ll.Node(-1)
    curr = head
    while list1 and list2:
        if list1.data <= list2.data:
            curr.next = ll.Node(list1.data)
            list1 = list1.next
        else:
            curr.next = ll.Node(list2.data)
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2 
    return head.next 

def mergeTwoLists(list1: Optional[LinkedList], list2: Optional[LinkedList]):
    # merged_list = approach_1(list1, list2)
    # merged_list = approach_2(list1, list2)
    merged_list = approach_3(list1, list2)
    return merged_list 

if __name__ == '__main__':
    nums_1 = [i for i in range(4,9)]
    nums_2 = [i for i in range(5)]
    linkedlist = LinkedList()
    list_1 = linkedlist.get_linked_list(nums_1)
    list_2 = linkedlist.get_linked_list(nums_2)
    merged_list = mergeTwoLists(list_1, list_2)
    linkedlist.print_custom_list(merged_list)
