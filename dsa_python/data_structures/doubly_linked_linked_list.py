class Node:
    def __init__(self, item, next, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def add(self, item):
        if self.n == 0:
            self.head = Node(item=item, next=None, prev=None)
            self.tail = None
        elif self.n == 1:
            new_node = Node(item=item, next=None, prev=None)
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = self.head.next
        else:
            new_node = Node(item=item, next=None, prev=None)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
        self.n += 1
        assert self.check() is True
    
    def remove(self, from_tail=True):
        # TODO: Add removal of any node instead of only from ends.
        if self.is_empty():
            raise ValueError("Doubly Linked list is already empty!")
        node = None
        if self.n == 1:
            node = self.head
            self.head = None
        if from_tail is True:
            node = self.tail
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node = self.head
            self.head = node.next
            self.head.prev = None
        self.n -= 1
        assert self.check() is True
        return node
    
    def check(self):
        if self.n < 0:
            return False
        if self.n == 0:
            if self.head is not None:
                return False
        return True
    
    def __str__(self):
        """Returns a string representation of the linked list"""
        items = []
        curr_node = self.head
        for _ in range(self.n):
            items.append(curr_node.item)
            curr_node = curr_node.next
        str_repr = " <=> ".join(items)
        if str_repr.strip() == '':
            str_repr = '<empty>'
        return str_repr
            
        
