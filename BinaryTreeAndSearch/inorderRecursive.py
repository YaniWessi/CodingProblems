class Node:
  def __init__(self, value):
    self.value = value
    self.right = None 
    self.left = None 

def inorder_traversal(node):
  if node is None:
    return 

  inorder_traversal(node.left) # Recursively traverse the left subtree
  print(node.value) # Process the current node 
  inorder_traversal(node.right) #Recursively traverse the right subtree 


# Example usage 
# Create a binary tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# Perform inorder traversal 
print("Inorder traversal:")
inorder_traversal(root)










#Inorder traversal find the a value:

class Node:
  def __init__(self, value):
    self.value = value 
    self.left = None 
    self.right = None 

def inorder_search(node, target):
  if node is None:
    return None 


  left_result = inorder_search(node.left, target)
  if left_result:
    return left_result   

  if node.value == target:
    return node 

  right_result = inorder_search(node.right, target)
  if right_result:
    return right_result  #Target found in the left subtree

 
 
  return None 


# Example usage 
# Create a binary tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Find node with value 5 
target_node = inorder_search(root, 5)


#inOrder Traverse 

def inOrderTraverse(tree, array):
  if tree is not None:
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
  return array 


  
  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

    def inorder_traversal(node, target):
      if node is None:
        return None

      left_result = inorder_traversal(node.left, target)
      if left_result is None:
        reutrn left_result

      if node.value == target:
        return None

     right_resut = inorder_traversal(node.right, target)
     if right_result is None:
      return right_result

  return None 