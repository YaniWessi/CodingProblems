
#Given pointers to the heads of two sorted linked lists, 
#merge them into a single, sorted linked list. Either head
#pointer may be null meaning that the corresponding list is empty. 

#video explanation on how to solve it visiually:https://www.youtube.com/watch?v=GfRQvf7MB3k&list=PLiQ766zSC5jMEpcGL0nSkfDM3paBP5FOE&index=4

#my Approach: 

# def mergeLists(head1, head2):
#   l1 = head1
#   l2 = head2

#   curr = None 

#   if l1.value > l2.value:
#     curr = l2 
#   elif l2.value > l1.value:
#     curr = l1 
#   else:
#     curr = l1 

#   while curr: 




# New approac on chatgpt: 
#  

class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None

def mergeLists(head1, head2):
  
  # Check if either list is empty
  if not head1:
    return head2
  if not head2:
    return head1
    
  # Initialize pointers
  l1 = head1
  l2 = head2
  merged_head = None
  merged_tail = None
    
  # Determine the head of the merged list
  if l1.data <= l2.data:
    merged_head = Node(l1.data)
    l1 = l1.next
  else:
    merged_head = Node(l2.data)
    l2 = l2.next
    
  merged_tail = merged_head
    
  # Merge the remaining nodes
  while l1 and l2:
    if l1.data <= l2.data:
      merged_tail.next = Node(l1.data)
      l1 = l1.next
    else:
      merged_tail.next = Node(l2.data)
      l2 = l2.next
    merged_tail = merged_tail.next
    
  # Append any remaining nodes from list1
  if l1:
    merged_tail.next = l1
    
  # Append any remaining nodes from list2
  if l2:
    merged_tail.next = l2
    
  return merged_head