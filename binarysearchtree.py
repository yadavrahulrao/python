class treenode :
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def traversal(node):
  if node is None:
    return
  traversal(node.left)
  print(node.data,end=",")
  traversal(node.right)

root = treenode(13)
nodeA = treenode(7)
nodeB = treenode(14)

nodeC = treenode(3)
nodeD = treenode(9)

nodeE = treenode(12)
nodeF = treenode(15)

nodeG = treenode(11)


def search(node , target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif node.data < target:
    return search(node.left,target)
  else :
    return search(node.right,target)

result = search(root,13)

if result :
  print(f"the node found at the {result.data}")
else :
  print("node is not valid ")

def insert(node , data):
  if node is None:
    return treenode(data)
  else :
    if  data < node.data:
      node.left = insert(node.left,data)
    elif data > node.data:
      node.right = insert(node.right,data)
    return node
insert(root,10)

def minvalue(node):
  curr = node
  if curr.left is not  None:
    curr = curr.left
  return curr

print("minimum value ",minvalue(root).data)
  

def delete(node , data):
  if not None:
    return None
  if data < node.data:
    node.left = delete(node.left,data)
  elif data > node.data:
    node.right = delete(node.right,data)
  else :
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None 
      return temp
    node.data = minvalue(node.right).data
    node.right = delete(node.right,node.data)
  return node
delete(root,15)