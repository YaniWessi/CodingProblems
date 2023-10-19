# traverse or search through a tree-like or graph-like data structures.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None 
    self.right = None 
  
  
  
def dfs(node):
  if not node:
    return 
  dfs(node.left) # Recur on the left subtree
  print(node.val) #Process the current node 
  dfs(node.right) #Recur on the right subtree 


# Usage 
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("Pre-order DFS:")

dfs(root)


#Using dfs for a problem
# You are given the root of a binary tree containing digits from 0 to 9 only. 
# Each root-to-leaf path in the tree represents a number. 
# For example, the root-to-leaf numbers. Test cases are generated so that the answer
# will fit in a 32-bit integer. 
# A leaf node is a node with no children. 

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None 

  def dfs(self, root, num):
    if not root:
      return 0 

    num = num * 10 + root.val 

    if not root.left and not root.right:
      return num 

    left_sum = self.dfs(root.left, num)  # Use 'self' to call the dfs method
    right_sum = self.dfs(root.right, num)  # Use 'self' to call the dfs method

    return left_sum + right_sum  # Return the sum of both branches
















# The Goal of a Stack: 

# Stacks 

#    - The goal of a stack is to store items in a last-in first-out order 

#      - Strength: all operations are fast. 
#        - Add an item to the top of the stack O(1)
#        - Remove an item from the top of the stack O(1)
#        - Inspect the item from the top of the stack without removing it O(1)
#        - Space complextiy linear 

#     - Good for tracking to conducting a depth search. 
#     - Stacks are very useful in Parsing strings. For instance if you have to check 
#     if a string is balanced or a palindrome or you're balancing parentheses you can
#     push and pop different part of the string 

#     -Weakness: It only can do a few things. Can do those few things very well. 















#dfs using a Stack 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_stack(root):
    if not root:
        return

    stack = [root]  # Initialize the stack with the root node

    while stack:
        current_node = stack.pop()  # Pop the top node from the stack
        print(current_node.val)     # Process the current node

        # Push child nodes onto the stack (right child first to ensure left child is processed first)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("DFS traversal using a stack:")
dfs_stack(root)
















# Stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Usage
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: Stack size: 3

print("Pop:", stack.pop())  # Output: Pop: 3
print("Pop:", stack.pop())  # Output: Pop: 2

print("Stack size after pops:", stack.size())  # Output: Stack size after pops: 1

print("Peek:", stack.peek())  # Output: Peek: 1