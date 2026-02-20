# queue data structure 

# queue = []


# queue.append('a')
# queue.append('b')
# queue.append('c')

# print(queue)

# peek = queue[0]
# print(peek)


# popped = queue.pop(0)
# print(popped)

# print(queue)

# isempty = not bool(queue)
# print(isempty)

# size = len(queue)
# print(size)



# queue using array using class
# class Solution:
#   def __init__(self):
#     self.q = []
  
#   def add(self,element):
#     self.q.append(element)
#   def peek(self):
#     return self.q[0]
#   def delete(self):
#     return self.q.pop(0)
#   def isempty(self):
#     return len(self.q) == 0
  
#   def size(self):
#     return len(self.q)

# s = Solution()
# s.add('a')
# s.add('b')
# s.add('c')
# s.add('d')

# print(s.q)

# print(s.peek())

# print(s.delete())

# print(s.q)

# print(s.isempty())

# print(s.size())



# queue using linked list 

class node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Solution:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  
  def add(self,element):
    new = node(element)
    if self.tail is None:
      self.head = self.tail = new
      self.length += 1
      return
    self.tail.next = new
    self.tail = new
    self.length += 1

  def delete(self):
    temp = self.head
    self.head = temp.next
    self.length -= 1
    if self.head is None:
      self.tail = None
    return temp.data

  def peek(self):
    return self.head.data
  
  def size(self):
    return self.length

  def queue(self):
    temp = self.head
    while temp:
      print(temp.data,end = '->')
      temp = temp.next 
    print()

s = Solution()
s.add('a')
s.add('b')
s.add('c')
s.add('d')

s.queue()

