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

class Stack :
  def __init__(self):
    self.stack = []

  def push(self,element):
    self.stack.append(element)

  def top(self):
    if self.isempty():
      return "stack is empty"
    return self.stack[-1]

  def delete(self):
    if self.isempty():
      return "stack is empty"
    return self.stack.pop()
  
  def isempty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

m = Stack()
m.stack.push('a')

  