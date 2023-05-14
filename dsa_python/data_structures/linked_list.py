class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.n = 0
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def add(self, item):
        if self.n == 0:
            self.head = Node(item=item, next=None)
        else:
            new_node = Node(item=item, next=None)
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
        self.n += 1
        assert self.check() is True
    
    def remove(self, from_tail=True):
        # TODO: Add removal of any node instead of only from ends.
        if self.is_empty():
            raise ValueError("Linked list is already empty!")
        node = None
        if self.n == 1:
            node = self.head
            self.head = None
        elif from_tail is True:
            node = self.head
            prev = None
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
        else:
            node = self.head
            self.head = node.next
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
        str_repr = " -> ".join(items)
        if str_repr.strip() == '':
            str_repr = '<empty>'
        return str_repr
        

        
