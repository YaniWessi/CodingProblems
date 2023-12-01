
class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None 

  def append(self, data):
    new_node = Node(data)

    if self.next:
      curr = self.next 
      while curr.next:
        curr = curr.next 
      curr.next = new_node
    else:
      self.next = new_node

  def delete(self, node):
    if self == node:
      if self.next:
        self.data = self.next.data 
        self.next = self.next.next 
      else:
        raise ValueError("Cannot delete the only node in the list.")
    else:
      curr = self 
      while curr.next:
        if curr.next == node:
          curr.next = curr.next.next 
          return
        curr = curr.next 
      raise ValueError("Node not found in the list")

  def get_node_data(self, index):
    curr = self 
    count = 0 

    while curr:
      if count == index:
        return curr.data 
      curr = curr.next 
      count += 1

    raise IndexError("Index out of range")




class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    self.head.append(value) 

  def delete(self, node):
    self.head.delete(node)

  def get_node_data(self, index):
    self.head.get_node_data(index)            
