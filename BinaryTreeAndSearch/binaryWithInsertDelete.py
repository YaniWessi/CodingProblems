

class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None 

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = Node(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = Node(value)
      else:
        self.right.insert(value)


  def search(self, value):
    if value == self.value:
      return self
    elif value < self.value:
      if self.left is None:
        return None
      else:
        self.value.search(value)
    else:
      if self.right is None:
        return None
      else:
        self.value.search(value)          


  def delete(self, node):
    if node < self.value:
      if self.left:
        self.left = self.left.delete(node)
    elif node > self.value:
      if self.right:
        self.right = self.right.delete(node)
    else:
      if self.left is None:
        return self.right
      elif self.right is None:
        return self.left 
      else:
        successor = self.right.find_minimum() 
        self.value = successor.value
        self.right = self.right.delete(successor.value)
    return self


def find_minimum(self):
  curr = self 
  while curr.left:
    curr = curr.left
  return curr    



class BST:
  def __init__(self, root):
    self.root = Node(root)

  def insert(self,value):
    self.root.insert(value)

  def delete(self,value):
    self.root.delete(value)     



#another approach

def contains(self, value):
  containsNode = self

  while containsNode is not None:
    if value < containsNode.value:
      containsNode = self.left
    elif value > containsNode.value:
      containsNode = self.right
    else:
      return True 

  return False              