#Pre order traversal on a binary tree: 

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None 
    self.right = None 

def preorder_traversal(node):
  if node is None:
    return 

  print(node.value) #Process the current node 
  preorder_traversal(node.left) # Recursively traverse the left subtree 
  preorder_traversal(node.right) # Recursively traverse the right subtree 


# Example usage
# Create a binary tree 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform preorder traversal 
print("Preorder traversal: ")
preorder_traversal(root)





#pre order traversal find the a value: 

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def preorder_search(node, target):

  if node is None:
    return None

  if node.value == target:
    return node # Found the target node 

  left_result = preorder_search(node.left, target) #Search in the left subtree
  if left_result is not None:
    return left_result #Target found in the left subtree 

  right_result = preorder_search(node.right, target) # Search in the right subtree
  if right_result is not None:
    return right_result #Target found in the right subtree

  return None  



# another approach to just put the values in an array: 

def preorder_search(tree, array):
  if tree is not None:
    array.append(tree.values())
    preorder_search(tree.left, array)
    preorder_search(tree.right, array)

  return array

  
    
class TreeNode:
  def __init__(self,value):
    self.value = value 
    self.left = None 
    self.right = None 

  def preorder_search(self, node, target):
    if node is not None:
      if node.value == target:
        return node

      result_left = self.preorder_search(node.left, target)
      if result_left is not None:
        return result_left
      result_right = self.preorder_search(node.right, target)
      return result_right
    return None                       