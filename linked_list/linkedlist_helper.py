from typing import Optional, List, Any

class LinkedList:
    def __init__(self, val: Any = 0, next: Optional['LinkedList'] = None):
        self.data = val
        self.next = next
    
    def create_root(self, data: int) -> 'LinkedList':
        self.root = LinkedList(data)
        return self.root
    
    def get_head(self) -> 'LinkedList':
        return self.root
    
    def get_linked_list(self, data: List[int]) -> 'LinkedList':
        if not data:
            raise ValueError('Cant create a linked list with empty data')
        
        head = self.create_root(data[0])
        current = head
        for element in data[1:]:
            current.next = LinkedList(element)
            current = current.next
        return head
    
    def __str__(self) -> str:
        """String representation of the linked list"""
        if self is None:
            raise ValueError('Cant print empty linked list')
        
        result = []
        current = self.get_head()
        while current:
            result.append(str(current.data))
            current = current.next
        print('->'.join(result))
        return
    
    def _get_length(self) -> int:
        cnt = 0
        current = self.get_head()
        while current:
            cnt += 1
            current = current.next
        return cnt
    
    def _get_middle(self) -> 'LinkedList':
        slow = fast = self.get_head()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        return slow

    def print_custom_list(head):
        current = head
        if current is None:
            raise ValueError('Head is None cant print linked list')
        
        while current:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end='->')
            current = current.next
    