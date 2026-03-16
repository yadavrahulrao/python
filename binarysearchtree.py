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

