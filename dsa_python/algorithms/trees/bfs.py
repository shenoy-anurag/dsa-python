from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BFS(root: TreeNode):
    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            print(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


def BFSLevel(root: TreeNode):
    queue = deque()
    queue.append(root)
    res = []

    while queue:
        level = []
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        res.append(level)
    return res


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    q = [root]
    res = []
    stop = False
    while not stop:
        next_level = []
        level = []
        for node in q:
            if node:
                next_level.extend([node.left, node.right])
                level.extend([node.val])
        if level:
            res.append(level)
        q = next_level
        if not next_level:
            stop = True
    return res


if __name__ == '__main__':
    """
    Tree:
            3
           / \
          9   20
             /  \
            15   7  
    """
    leaf15 = TreeNode(15, None, None)
    leaf7 = TreeNode(7, None, None)
    node20 = TreeNode(20, left=leaf15, right=leaf7)
    node9 = TreeNode(9, None, None)
    root = TreeNode(3, left=node9, right=node20)

    BFS(root)
    res_bfs = BFSLevel(root)
    print(res_bfs)
    res = levelOrder(root)
    print(res)
