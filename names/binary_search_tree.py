import sys
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
            if self.value == target:
                return True
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
            

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------
    


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        que = Queue()
        que.enqueue(node)

        while que.len() > 0:
            curr = que.dequeue()
            print(curr.value)
            if curr.left:
                que.enqueue(curr.left)
            if curr.right:
                que.enqueue(curr.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            curr = stack.pop()
            print(curr.value)
            if curr.left:
                stack.push(curr.left)
            if curr.right:
                stack.push(curr.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
