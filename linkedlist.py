#traversal of a linked list

# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def traverseAndPrint(head):
#   currentNode = head
#   while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
#   print("null")

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# traverseAndPrint(node1)


# find the lowest value in a linked list 

# class Node:
#   def __init__(self,data):
#     self.data = data
#     self.next = None
  
# def thelowest(head):
#   minvalue = head.data
#   curr = head.next
#   while curr:
#     if curr.data < minvalue:
#       minvalue = curr.data
#     curr = curr.next
#   return minvalue

# n1 = Node(5)
# n2 = Node(11)
# n3 = Node(4)
# n4 = Node(1)
# n5 = Node(3)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


# print(thelowest(n1))



# delete a node from a linked list 

# class Node :
#   def __init__(self,data):
#     self.data = data
#     self.next = None

# def traverse(head):
#   curr = head 
#   while curr:
#     print(curr.data,end='-->')
#     curr = curr.next
#   print("null")

# def deletenode(head,node):
#   if head == node:
#     return head.next
#   curr = head
#   while curr.next and curr.next != node:
#     curr = curr.next
  
#   if curr.next == None:
#     return head
  
#   curr.next = curr.next.next
#   return head

# n1 = Node(2)
# n2 = Node(4)
# n3 = Node(5)
# n4 = Node(6)
# n5 = Node(8)

# n1.next = n2 
# n2.next = n3
# n3.next = n4
# n4.next = n5

# traverse(n1)

# n1 = deletenode(n1,n4)

# traverse(n1)



# insert a node in a linked list 


class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
  
def traverse(head):
  curr = head
  while curr:
    print(curr.data,end="-->")
    curr = curr.next
  print("null")

def insertnode(head,node,pos):
  if pos == 1:
    node.next = head
    return node
  curr = head
  for _ in range(pos-2):
    if curr is None:

      break
    curr = curr.next
  node.next = curr.next
  curr.next = node
  return head

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2 
n2.next = n3
n3.next = n4 
n4.next = n5 

traverse(n1)

node = Node(67)

n1 = insertnode(n1,node , 3)

traverse(n1)