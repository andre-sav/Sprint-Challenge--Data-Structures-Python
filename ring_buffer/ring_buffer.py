from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity is not reached, simply add item to the DDL
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if capacity is reached, overwrite oldest with newest
        # need to track the next oldest in list, self.current tracks oldest
        else:
        # oldest will start at head, must track
            self.current.value = item
            if self.current.next != None:
                self.current = self.current.next
            else:
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # return all elements in the buffer in a list in their given order,
        # except if the element equates to none
        current = self.storage.head
        for _ in range(len(self.storage)):
            if current.value != None:
                list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0
        self.temp = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1

        if self.current == self.capacity:
            self.current = 0

    def get(self):
        final = []
        for i in self.storage:
            if i is not None:
                final.append(i)

        return final
