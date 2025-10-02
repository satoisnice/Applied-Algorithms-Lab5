class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"TreeNode(contents={repr(self.contents)}, parent-contents={repr(self.parent.contents if self.parent else 'NOPARENT')}, num-children={len(self.children)})"

    def appendChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.append(new_node)
        return new_node        

    def prependChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.insert(0, new_node)

    def findRoot(self):
        current_node = self
        while current_node.parent is not None:
            current_node = current_node.parent
            #sometha reassign current to parent
        return current_node

    def findLeftmostLeaf(self):
        current_node = self
        while len(current_node.children) != 0:
            current_node = current_node.children[0]
        return current_node
        
    def findRightmostLeaf(self):
        current_node = self
        while len(current_node.children) != 0:
            current_node = current_node.children[-1]
        return current_node
    
    def dfs(self, node):
        root = node.findRoot()
        stack = []
        out = []
        stack.append(root)
        while len(stack) != 0:
            top = stack.pop()
            out.append(top)
            for children in top.children:
                stack.append(top.children[-1])

