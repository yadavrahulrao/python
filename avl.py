class Treenode :
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

def getHeight(node):
  if not node:
    return 0
  return node.height

def getBalance(node):
  if not node:
    return 0
  return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
  print("rotate right on node :",y.data)
  x = y.left
  t2 = x.right
  x.right = y
  y.left = t2
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  return x


def leftRotate(x):
  print("rotate on left node :",x.data)
  y = x.right
  t2 = y.left
  y.left = x
  x.right = t2
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  return y


def insert(node,data):
  if not node:
    return Treenode(data)

  if data < node.data :
    node.left = insert(node.left,data)
  elif data > node.data :
    node.right = insert(node.right,data)


  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)

  if balance > 1 and getBalance(node.left) >= 0 :
    return rightRotate(node)
  
  if balance > 1 and getBalance(node.left) < 0 :
    node.left = leftRotate(node.left)
    return rightRotate(node)

  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)
  
  if balance < -1 and getBalance(node.right) > 0 :
    node.right = rightRotate(node.right)
    return leftRotate(node)
  
  return node

# for deleting a node 

def minValue(node):
  curr = node
  while curr.left is not None:
    curr = curr.left
  return curr

def delete(node,data):
  if not node :
    return node
  if data < node.data:
    node.left = delete(node.left,data)
  elif data > node.data:
    node.right = delete(node.right,data)
  
  else :
    if node.left is None:
      temp = node.right
      node = None
      return temp
    elif node.right is None:
      temp = node.left
      node = None
      return temp
    temp = minValue(node.right)
    node.data = temp.data
    node.right = delete(node.right,temp.data)
  return node



def traversal(node):
  if node is None:
    return
  traversal(node.left)
  print(node.data,end=",")
  traversal(node.right)


root = None
letter = ['C','B','E','A','D','H','G','F']
for i in letter:
  root = insert(root,i)

traversal(root)

