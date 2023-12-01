Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

headA refers to 1 -> 3 -> 7 -> NULL

headB refers to 1 -> 2 -> NULL

The new list is 

1 -> 1 -> 2-> 3->7-> NULL



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
    head = None
    curr = None
    
    # Determine the head of the merged list
    if l1.data <= l2.data:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    
    # Initialize the current pointer to the head of the merged list
    curr = head
    
    # Merge the lists
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    # If one of the lists is not fully processed, append the remaining elements
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    
    return head

# Example usage:
# headA refers to 1 -> 3 -> 7 -> NULL
# headB refers to 1 -> 2 -> NULL
# The merged list is 1 -> 1 -> 2 -> 3 -> 7 -> NULL