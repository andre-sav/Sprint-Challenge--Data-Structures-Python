class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    # def reverseUtil(self, curr, prev): 
          
    #     # If last node mark it head 
    #     if curr.next is None : 
    #         self.head = curr  
              
    #         # Update next to prev node 
    #         curr.next = prev 
    #         return 
          
    #     # Save curr.next node for recursive call 
    #     next = curr.next
  
    #     # And update next  
    #     curr.next = prev 
      
    #     self.reverseUtil(next, curr)  
    # # This function mainly calls reverseUtil() 
    # # with previous as None 
    # def reverse(self): 
    #     if self.head is None: 
    #         return 
    #     self.reverseUtil(self.head, None) 
  

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # returns if no node
        if self.head is None:
            return
        # if the next node is none, sets the head as current node and its next node as previous
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
            return
        # recursive call which submits the next node and the previous node as arguments
        self.reverse_list(node.next_node, node)
        # finishes by pointing the last node backwards
        node.next_node = prev
        