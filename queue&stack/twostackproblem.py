# implement this questions " A queue is an abstract data type that maintains the order in which elements were added to it,
# allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a 
# First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been 
# waiting the longest) is always the first one to be removed.

# A basic queue has the following operations:

# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query
# is one of the following  types:

# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue." 

class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, element):
        self.enqueue_stack.append(element)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None  # Queue is empty
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None  # Queue is empty
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

# Process queries
def process_queries(queries):
    queue = QueueUsingStacks()
    results = []

    for query in queries:
        query_type = query[0]

        if query_type == 1:
            # Enqueue operation
            element = query[1]
            queue.enqueue(element)
        elif query_type == 2:
            # Dequeue operation
            queue.dequeue()
        elif query_type == 3:
            # Print front element
            results.append(queue.peek())

    return results

# Example usage:
queries = [
    (1, 42),
    (2,),
    (1, 14),
    (3,),
    (1, 28),
    (3,),
]

results = process_queries(queries)
print(results)  # Output: [14, 28]
