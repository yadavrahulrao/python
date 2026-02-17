# LIFO

# stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# print("push then",stack)

# print("peek element",stack[-1])

# stack.pop()
# print("after pop",stack)

# emt = not bool(stack)
# print(emt)

# print(len(stack))


#stack using array and class 

# class Stack :
#   def __init__(self):
#     self.stack = []

#   def push(self,element):
#     self.stack.append(element)

#   def top(self):
#     if self.isempty():
#       return "stack is empty"
#     return self.stack[-1]

#   def delete(self):
#     if self.isempty():
#       return "stack is empty"
#     return self.stack.pop()
  
#   def isempty(self):
#     return len(self.stack) == 0

#   def size(self):
#     return len(self.stack)

# m = Stack()
# m.push('a')
# m.push('b')
# m.push('c')

# print(m.stack)

# m.delete()
# print(m.stack)

  
#  stack using linked list 


# class node:
#   def __init__(self,value):
#     self.value = value
#     self.next = None

# class Stack:
#   def __init__(self):
#     self.head = None
#     self.size = 0

#   def push(self,value):
#     new = node(value)
#     if self.head :
#       new.next = self.head
#     self.head = new
#     self.size += 1

#   def isempty(self):
#     return self.size == 0

#   def delete(self):
#     if self.isempty:
#       print("stack is empty")

#     poped = self.head
#     self.head =  self.head.next 
#     self.size -= 1
#     return poped.value

#   def top(self):
#     if self.isempty:
#       print("stack is empty")
#     return self.head.value

#   def stack_size(self):
#     return self.size

#   def traverse(self):
#     curr = self.head
#     while curr :
#       print(curr.value,end="-->")
#       curr = curr.next 
#     print()

# m = Stack()

# m.push('a')
# m.push('b')
# m.push('c')
# m.push(2)

# print(m.traverse())

# print(m.stack_size())




#question 

class Stack:
  def __init__(self):
    
    self.stack = ["a","b","c"]

  def push(self,element):
    self.stack.append(element)
  
  # def isempty(self):
  #   return len(self.stack) == 0

  def delete(self):
    
    return self.stack.pop(0)

  def peek(self):
    return self.stack[-1]


m = Stack()
m.push('d')
print(m.stack)

m.delete()
print(m.stack)

print(m.peek())