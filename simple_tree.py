class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"TreeNode(contents={repr(self.contents)}, parent-contents={repr(self.parent.contents if self.parent else 'NOPARENT')}, num-children={len(self.children)}, children={repr([child.contents for child in self.children])})"

    def appendChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.append(new_node)
        return new_node        

    def prependChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.insert(0, new_node)
        return new_node

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
    
    def dfs(self):
        root = self.findRoot()
        stack = [root]
        out = []

        while stack:
            top = stack.pop()
            out.append(top.contents)
            for child in reversed(top.children):
                stack.append(child)
        return out

def case1():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.appendChild("B")
    root.appendChild("C")
    root.appendChild("D")

    print("\ncase1")

    # once you have implemented appendChild, the first print should work
    print("I hope the root has 3 children")
    print(root)

    # once you're nearly done, these prints should work too
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case2():
    # This is supposed to make the same tree as last time, but differently:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.prependChild("C")
    root.appendChild("D")
    root.prependChild("B")

    print("\ncase2")

    # once you have implemented prependChild, the first print should work
    print("I hope the root has 3 children")
    print(root)

    # once you're nearly done, these prints should work too
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case3():
    # This is supposed to make this tree:
    #
    #            A
    #         /  |  \
    #        B   C   D
    #        |      / \
    #        E     F   G
    #
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    g = d.prependChild("G")
    f = d.prependChild("F")
    e = b.appendChild("E")

    print("\ncase3")


    # and all of the following should print the root node (each one prints itself and then the root):
    for node in [root, b, c, d, e, f, g]:
        r = node.findRoot()
        print("node:", node, "   found root:   ", r, "   is correct tho? ", r == root)

    # and the following should be able to find E:
    print("findLeftmostLeaf of root, should be E:", root.findLeftmostLeaf())
    # and the following should be able to find F:
    print("findLeftmostLeaf of D, should be F:", d.findLeftmostLeaf())
    # and the following should be able to find G:
    print("findRightmostLeaf of D, should be G:", d.findRightmostLeaf())

def case4():
    #dfs (pre-order) test
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    g = d.prependChild("G")
    f = d.prependChild("F")
    e = b.appendChild("E")

    print(e.dfs())

def main(args):
    case1()
    case2()
    case3()
    case4()



if __name__ == '__main__':
    import sys
    main(sys.argv[1:])