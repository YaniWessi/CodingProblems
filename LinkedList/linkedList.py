# class Node:
#   def __init__(self, data):
#     self.data = data 
#     self.next = None 

# class Linkedlist:
#   def __init__(self):
#     self.head = None 

#   def append(self, data):
#     new_node = Node(data)

#     if self.head is None:
#       self.head = new_node
#     else:
#       curr = self.head
#       while curr.next:
#         curr = curr.next
#       curr.next = new_node


#   def prepend(self, data):
#     new_node = Node(data)
#     new_node.next = self.head 
#     self.head = new_node

#   def delete(self, data):
#     if self.head is None:
#       return

#     if self.head.data == data:
#       self.head = self.head.next 
#       return 

#     curr = self.head 
#     while curr.next:
#       if curr.next.data == data:
#         curr.next = curr.next.next 
#         return
#       curr = curr.next 


#   def print_list(self):
#     curr = self.head
#     while curr:
#       print(curr.data, end=" ")
#       curr = curr.next 

#     print()                        


# # Create a new linked list 
# my_list = Linkedlist()


# # Append some elements 
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)


# # Prepend an element
# my_list.prepend(5)


# #Delete an element
# my_list.delete(20)


# # Print the list
# my_list.print_list()


class ListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

  def append(self, data):
    new_node = ListNode(data)

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
      raise ValueError("Node not found in the list.")
  
  def access(self, value):
    curr = self  # Start at the beginning of the linked list
    while curr is not None:
        if curr.value == value:
            return curr  # Found the node with the given value
        curr = curr.next
    raise ValueError("Value not in linked list")    

class LinkedList:
  def __init__(self, data):
    self.head = ListNode(data)

  def append(self, data):
    self.head.append(data)

  def delete(self, node):
    self.head.delete(node)

  def get_data(self, value):
    self.head.get_data(value)








  def delete(self, node):
    if self == node: # <--- if the node to be deleted is the head node 
      if self.next:  # <--- if the head node has a "next" node, you copy the data of the "next" node into 
        self.data = self.next.data # you copy the data of the "next" node into the current node
        self.next = self.next.next #and update the "next" reference to skip the next node, effectively Deleteing
      else:
        raise ValueError("Cannot delete the only node in the list") # else the head has no next and we cant delete the only node in the list
    else: #<-- if the node to be deleted is not the head node 
      curr = self  # <-- starting from the head 
      while curr.next: # You traverse the linked list starting from the head 
        if curr.next == node: #until you find the node just before the node to be deleted
          curr.next = curr.next.next # Once you find the node just before the target node, you update the "next" reference of the previous node to skip the target node, effectively deleting it. 
          return 
        curr = curr.next 
      raise ValueError("Node not found in the list") # if the target node is not found during the traversal, you raise a 'ValueError' because the node to be deleted is not in the list. 
      
# A linked list is best for inserting and deleting items. its deletes in an O(1)
# in the best case and O(n) in the worst case  
# Linear time complextiy. Secondly it deletes items in an O(1) constant time in 
# the best case and deletes O(n) in the worst case. accessing and search are both O(n)
# in the best and worst case. 

class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None 

  def insert(self, value):
    new_node = Node(value)
    
    if self.next:
      curr = self.next 
      while curr.next:
        curr = curr.next
      curr.next = new_node
    else:
      self.next = new_node

  def delete(self, node):
    if self.value == node:
      if self.next:
        self.data = self.next.data 
        self.next = self.next.next
      else:
        raise ValueError("Can not delete only node in list")
    else:
      curr = self 
      while curr.next:
        if curr.next == node:
          curr.next = curr.next.next
          return 
        raise ValueError("The node does not exist in the list")


class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None 
  
  def insert(self, value):
    new_node = Node(value)

    if self.next:
      curr = self.next 
      while curr.next:
        curr = curr.next
      curr.next = new_node
    else:
      self.next = new_node

  def delete(self, node):
    if self.value == node:
      if self.next:
        self.value = self.next.value
        self.next = self.next.next 
      else:
        raise ValueError("can not delete only node in the list")
    else:
      curr = self 
      while curr.next:
        if curr.next == node:
          curr.next = curr.next.next
          return
        curr = curr.next
      raise ValueError("Node could not be found")
