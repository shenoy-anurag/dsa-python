class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []
    
    def __str__(self) -> str:
        return str(self.value)

class Tree:
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def display(self):
        self.show_children(self.root)
    
    def show_children(self, node):
        print(node)
        # if node.children:
        #     print([str(n) for n in node.children])
        for n in node.children:
            self.show_children(n)


if __name__ == '__main__':
    t = Tree(root=TreeNode(value=1))
    t.root.children.append(TreeNode(2))
    t.root.children.append(TreeNode(3))
    t.root.children.append(TreeNode(4))
    t.root.children.append(TreeNode(5))
    t.root.children[0].children.append(TreeNode(6))
    t.root.children[0].children.append(TreeNode(7))
    t.root.children[1].children.append(TreeNode(8))
    t.root.children[1].children.append(TreeNode(9))
    t.root.children[2].children.append(TreeNode(10))
    t.root.children[2].children.append(TreeNode(11))
    t.display()
