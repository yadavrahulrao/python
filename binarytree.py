class treenode :
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

root = treenode('r')
nodeA = treenode('a')
nodeB = treenode('b')
nodeC = treenode('c')
nodeD = treenode('d')
nodeE = treenode('e')
nodeF = treenode('f')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

print("root right left data :",root.right.left.data)


def preorder(node):
  if node is None:
    return
  print(node.data,end=", ")
  preorder(node.left)
  preorder(node.right)


def inorder(node):
  if node is None:
    return 
  inorder(node.left)
  inorder(node.data,end=" ,")
  inorder(node.right)


def postorder(node):
  if node is None:
    return
  postorder(node.left)
  postorder(node.right)
  postorder(node.data,end = " ,")