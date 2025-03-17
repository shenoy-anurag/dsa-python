"""
    Binary Trees:

    Trees whose nodes can only have AT MOST two children.

    Other rules that apply to Trees apply to Binary trees as well (such as no cycles allowed).
"""


from typing import Optional


class BinaryTreeNode:
    # def __init__(self, value) -> None:
    def __init__(self, value, parent=None) -> None:
        self.parent = parent
        self.value = value
        self.left = None  # left child
        self.right = None  # right child


class BinaryTree:
    def __init__(self, root: BinaryTreeNode) -> None:
        self.root = root
        self.empty_leaf_parent = root
        self.num_nodes = 1 if root else 0

    # def recursive_find_empty_parent(self, node: BinaryTreeNode):
    #     if not node.right:
    #         return node
    #     else:
    #         child = node.right
    #         if child.left and child.right:
    #             return self.recursive_find_empty_parent(node.parent)
    #         else:
    #             return node

    # def find_empty_leaf_parent(self):
    #     if self.empty_leaf_parent == self.root:
    #         return self.root
    #     else:
    #         pass


    # def add_node(self, value, parent: BinaryTreeNode = None):
    #     if not parent:
    #         node = BinaryTreeNode(parent=self.empty_leaf_parent, value=value)
    #         if not self.empty_leaf_parent.left:
    #             node.parent = self.empty_leaf_parent
    #             self.empty_leaf_parent.left = node
    #         else:
    #             node.parent = self.empty_leaf_parent
    #             self.empty_leaf_parent.right = node
    #     else:
    #         node = BinaryTreeNode(parent=parent, value=value)
    #         if not parent.left:
    #             node.parent = parent
    #             parent.left = node
    #         else:
    #             node.parent = parent
    #             parent.right = node

    # def add_node(self, value):
    #     node = BinaryTreeNode(parent=self.empty_leaf_parent, value=value)
    #     if not self.empty_leaf_parent.left:
    #         node.parent = self.empty_leaf_parent
    #         self.empty_leaf_parent.left = node
    #     else:
    #         if not self.empty_leaf_parent.right:
    #             node.parent = self.empty_leaf_parent
    #             self.empty_leaf_parent.right = node
    #         else:
    #             self.empty_leaf_parent = 
    #             node.parent = self.empty_leaf_parent
    #             self.empty_leaf_parent.left = node

    def insert_left(self, node: BinaryTreeNode, value):
        if node.left is None:
            node.left = BinaryTreeNode(value=value, parent=node)
        else:
            new_node = BinaryTreeNode(value=value)
            new_node.left = node
            new_node.parent = node.parent
            node.parent = new_node
    
    def insert_right(self, node: BinaryTreeNode, value):
        if node.right is None:
            node.right = BinaryTreeNode(value=value, parent=node)
        else:
            new_node = BinaryTreeNode(value=value)
            new_node.right = node
            new_node.parent = node.parent
            node.parent = new_node

    def in_order_traversal(self, node: BinaryTreeNode = None):
        if not node:
            self._iter_in_order(self.root)
        else:
            self._iter_in_order(node)

    def _iter_in_order(self, node: BinaryTreeNode):
        if not node:
            return
        self._iter_in_order(node.left)
        print(node.value)
        self._iter_in_order(node.right)

    def pre_order_traversal(self, node: BinaryTreeNode = None):
        if not node:
            self._iter_pre_order(self.root)
        else:
            self._iter_pre_order(node)

    def _iter_pre_order(self, node: BinaryTreeNode):
        if not node:
            return
        print(node.value)
        self._iter_pre_order(node.left)
        self._iter_pre_order(node.right)

    def is_balanced(self):
        """Return the tree height + 1 if balanced, -1 otherwise."""
        return self._is_balanced(self.root)

    def _is_balanced(self, root: Optional[BinaryTreeNode]) -> int:
        """Return the tree height + 1 if balanced, -1 otherwise.

        :param root: Root node of the binary tree.
        :type root: binarytree.Node | None
        :return: Height if the binary tree is balanced, -1 otherwise.
        :rtype: int
        """
        if root is None:
            return 0
        left = self._is_balanced(root.left)
        if left < 0:
            return -1
        right = self._is_balanced(root.right)
        if right < 0:
            return -1
        return -1 if abs(left - right) > 1 else max(left, right) + 1


if __name__ == '__main__':
    root_node = BinaryTreeNode(value=1)
    bt = BinaryTree(root=root_node)
    bt.root.left = BinaryTreeNode(value=2)
    bt.root.right = BinaryTreeNode(value=3)
    bt.root.left.left = BinaryTreeNode(value=4)
    bt.root.left.right = BinaryTreeNode(value=5)
    bt.root.right.left = BinaryTreeNode(value=6)
    bt.in_order_traversal()
    print("--------------")
    bt.pre_order_traversal()


