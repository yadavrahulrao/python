class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    if not head or not head.next or not head.next.next:
        return
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_half = slow.next
    slow.next = None  
    prev = None
    while second_half:
        next_node = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = next_node
    first_half = head
    second_half = prev 
    
    while second_half:
      
        temp1, temp2 = first_half.next, second_half.next
        
        
        first_half.next = second_half
        second_half.next = temp1
        
      
        first_half = temp1
        second_half = temp2

def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

head = create_linked_list([1, 2, 3, 4, 5, 6])
print("Original List:")
print_list(head)

reorderList(head)

print("Reordered List:")
print_list(head)
