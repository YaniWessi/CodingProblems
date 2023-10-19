
# We are using a queue here because using a queue is the best use of of a queue because
# The goal of a queue is to store things in a first-in first-out order. 
#Conducting a breath - first search is best down using a queue. You can keep track of the nodes you need to visit          
#Web sever also use queues to manage page request from users. The first request will resolve first 

#Weakness of a queue is that it is a very targeted data structure that is designed to be used
# to do few things very well. 

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None 

  def bfs(self, node):
    if not node:
      return 

    queue = [node] # Initialize a queue with the root node 

    while queue:
      curr = queue.pop(0)  # Dequeue the front node 
      print(curr)          # Process the current node 

      if curr.left:
        queue.append(curr.left)  # Enqueue the left child 
      if curr.right:
        queue.append(curr.right) # Enqueue the right child 


#usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)        


class BST:
  def __init__(self, root):
    self.root = TreeNode(root)


  def bfs(self, root):
    self.root.bfs(root)










# queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Usage
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: Queue size: 3

print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 2

print("Queue size after dequeues:", queue.size())  # Output: Queue size after dequeues: 1