class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    stack1, stack2 = [], []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
    carry = 0
    result = None
    while stack1 or stack2 or carry :
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        total = val1 + val2 + carry
        carry = total // 10  
        new_node = ListNode(total % 10)  
        new_node.next = result
        result = new_node
    return result
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()
l1 = create_linked_list([7, 2, 4, 3])
l2 = create_linked_list([5, 6, 4])
print("l1:")
print_linked_list(l1)
print("l2:")
print_linked_list(l2)
result = addTwoNumbers(l1, l2)
print("Result:")
print_linked_list(result)
