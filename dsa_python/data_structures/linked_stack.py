class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedStack:
    def __init__(self):
        self.n = 0
        self.first = None
        assert self.check() is True

    def is_empty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        self.first = Node(item, old_first)
        self.n += 1
        assert self.check() is True

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        assert self.check() is True
        return item

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        item = self.first.item
        return item

    def check(self):
        if self.n < 0:
            return False
        if self.n == 0:
            if self.first is not None:
                return False
        elif self.n == 1:
            if self.first is None:
                return False
            if self.first.next is not None:
                return False
        else:
            if self.first is None:
                return False
            if self.first.next is None:
                return False
        return True

    def __str__(self):
        """Returns a string representation of the stack"""
        items = []
        curr_node = self.first
        for i in range(self.n):
            items.append(curr_node.item)
            curr_node = curr_node.next
        str_repr = " -> ".join(reversed(items))
        return str_repr
