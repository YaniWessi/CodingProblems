class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def buildTree(arr):
  if not arr:
    return None

  root = TreeNode(arr[0])
  for num in arr[1:]:
    curr = root.left
    while True:       