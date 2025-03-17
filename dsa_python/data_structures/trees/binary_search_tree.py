"""
    -------------------
    Binary Search Trees
    -------------------

    Binary trees which can be used to search for a particular number quickly.

    The properties that separate a binary search tree from a regular binary tree is

    1. All nodes of left subtree are less than the root node
    2. All nodes of right subtree are more than the root node
    3. Both subtrees of each node are also BSTs i.e. they have the above two properties

    Other rules that apply to Binary trees apply to Binary Search trees as well 
    (such as no cycles allowed, and only two nodes per parent).

    Time Complexity:
    Search: O(log(N))

    Space Complexity:
    O(3N)

    BST Applications:
    - In multilevel indexing in the database
    - For dynamic sorting
    - For managing virtual memory areas in Unix kernel

"""


from typing import Optional, Union


class Node:
    def __init__(self, value: Union[int, float]) -> None:
        self.data = value
        self.left = None  # left child
        self.right = None  # right child

class BinarySearchTree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def insert(self, value: Union[int, float]):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value=value)

    def _insert(self, node: Node, value: Union[int, float]):
        if value < node.data:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value: Union[int, float]):
        return self._search(self.root, value=value)

    def _search(self, node: Node, value: Union[int, float]):
        if not node:
            return None
        if value == node.data:
            return node.data
        if value < node.data:
            return self._search(node.left, value)
        if value > node.data:
            return self._search(node.right, value)
        
    def _is_leaf(self, node: Node):
        return node.left is None and node.right is None
    
    def is_empty(self):
        return self.root is None
    
    def _in_order_successor(self, root: Node):
        successors = []
        node = root.right
        successors.append((node.data))
        stop = False
        while not stop:
            if self._is_leaf(node):
                successors.append((node.data))
                stop = True
            else:
                if node.left:
                    node = node.left
                else:
                    node = node.right
                successors.append((node.data))
        return min(successors)
    
    def delete(self, value):
        if self._is_leaf(self.root):
            if value == self.root.data:
                self.root = None
                return value
            else:
                return None
        else:
            return self._delete(self.root, value=value)
        
    def _delete(self, node: Node, value: Union[int, float]):
        parent = None
        # search key in the BST and set its parent pointer
        while node and node.data != value:
            parent = node
            if value < node.data:
                node = node.left
            else:
                node = node.right
    
        # return if the key is not found in the tree
        if node is None:
            return node

        # Case 1: Node to be removed is a Leaf node.
        if self._is_leaf(node):
            # if the node is not the root node, then remove it using its parent node.
            if node != self.root:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            # if the tree has only a root node, set it to None
            else:
                self.root = None
        # Case 3: Node to be removed has two children.
        elif node.left and node.right:
            successor = self._in_order_successor(node)
            self._delete(node, value=successor)
            node.data = successor
        # Case 2: Node to be removed has a single child.
        else:
            # choose a child node
            if node.left:
                child = node.left
            else:
                child = node.right

            # if the node to be deleted is not a root node, set its parent
            # to its child
            if node != self.root:
                if node == parent.left:
                    parent.left = child
                else:
                    parent.right = child
    
            # if the node to be deleted is a root node, then set the root to the child
            else:
                self.root = child

    def in_order_traversal(self, node: Node = None):
        if not node:
            self._iter_in_order(self.root)
        else:
            self._iter_in_order(node)

    def _iter_in_order(self, node: Node):
        if not node:
            return
        self._iter_in_order(node.left)
        print(node.data)
        self._iter_in_order(node.right)

    def pre_order_traversal(self, node: Node = None):
        if not node:
            self._iter_pre_order(self.root)
        else:
            self._iter_pre_order(node)

    def _iter_pre_order(self, node: Node):
        if not node:
            return
        print(node.data)
        self._iter_pre_order(node.left)
        self._iter_pre_order(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree(root=Node(8))
    bst.insert(3)
    bst.insert(10)
    bst.insert(14)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    bst.in_order_traversal()
    print(bst.search(6))
    print(bst.search(5))
    print(bst.search(8))
    # print("Tree before case 1 deletion:")
    # bst.in_order_traversal()
    # bst.delete(7)
    # print("deleted")
    # bst.in_order_traversal()
    # print("Tree before case 2 deletion:")
    # bst.in_order_traversal()
    # bst.delete(6)
    # print("deleted")
    # bst.in_order_traversal()
    print("Tree before case 3 deletion:")
    bst.in_order_traversal()
    bst.insert(4)
    bst.delete(3)
    print("deleted")
    bst.in_order_traversal()
