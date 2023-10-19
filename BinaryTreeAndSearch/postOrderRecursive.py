
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None 
    self.right = None


def postorder_traversal(node):
  if node is None:
    return

  postorder_traversal(node.left)  # Recursively traverse the left subtree
  postorder_traversal(node.right) # Recursively traverse the right subtree
  print(node.value) # Process the current node 


# Example usage
# Create a binary tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform postorder traversal 
print("Postorder traversal:")
postorder_traversal(root)










#post order traversal find the a value:

class Node:
  def __init__(self, value):
    self.value = value 
    self.left = None 
    self.right = None 

def postorder_search(node, target):
  if node is None:
    return None 

  right_result = postorder_search(node.right, target)
  if right_result is not None:
    return right_result  #Target found in the left subtree

  left_result = postorder_search(node.left, target)
  if left_result is not None:
    return left_result 


  if node.value == target:
    return node 

  return None 


# Example usage 
# Create a binary tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Find node with value 5 
target_node = postorder_search(root, 5)

    


# another example postOrder traverse 

def postOrderTraverse(tree, array):
  if tree is not None:
    postorder_traversal(tree.left, array)
    postorder_traversal(tree.right, array)
    array.append(tree.value)

  return array 