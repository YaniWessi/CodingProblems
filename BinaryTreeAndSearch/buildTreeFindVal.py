# use trace 

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right 


def build_tree(arr):
  if not arr:
    return None

  mid = len(arr) // 2 

  root = TreeNode(arr[mid])
  root.left = build_tree(arr[:mid])
  root.right = build_tree(arr[mid+1:])
  return root



def find_val(root,tget):
  stack = []
  curr = root 

  while curr or stack:
    while curr:
      stack.append(curr)
      curr = curr.left
    curr = stack.pop()
    if curr.val == tget:
      return curr.val
    curr = curr.right 
  return None   



nums = [6, 4, 5, 3, 7, 10]

target = 5

my_tree = build_tree(nums)

print(find_val(my_tree,target))










