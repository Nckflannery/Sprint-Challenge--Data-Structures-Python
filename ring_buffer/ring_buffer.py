from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Set initial spot
        if not self.current:
            self.current = self.storage.head
        # If we are at capacity, replace oldest item
        if self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next
        # Else, add to tail
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # Create pointer to iter through self.storage, start at oldest (head)
        pointer = self.storage.head
        while pointer:
            # Append pointer value to list, and increment using .next
            list_buffer_contents.append(pointer.value)
            pointer = pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.index = 0
        self.replacer_index = 0
        self.max_index = self.capacity - 1

    def append(self, item):
        if self.index < self.capacity:
            self.storage[self.index] = item
            self.index += 1
        else:
            self.storage[self.replacer_index] = item
            if self.replacer_index < self.max_index:
                self.replacer_index += 1
            else:
                self.replacer_index = 0
        
    def get(self):
        if self.index <= self.capacity:
            return self.storage[:self.index]
        else:
            return self.storage
