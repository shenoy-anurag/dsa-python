"""
This is an implementation of the Stack datastructure using a list.
"""

from dsa_python.data_structures.stacks.base_stack import BaseStack


class Stack(BaseStack):
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        item = self.items.pop(-1)
        return item
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        item = self.items[-1]
        return item
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        """Returns a string representation of the stack"""
        str_repr = ",".join(self.items) + " <- top"
        return str_repr

    
