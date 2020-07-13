"""

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self, node, value):
        if node == None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left == None:
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if node.right == None:
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

def serialize(node):
    serialize_string = []
    def process(node):
        if not node:
            serialize_string.append("*")
        else:
            serialize_string.append(str(node.value))
            process(node.left)
            process(node.right)
    process(node)
    return ','.join(serialize_string)

def deserialize(string):
    values = iter(string.split(","))
    def process():
        value  = next(values)
        if value == "*":
            return None
        node = Node(int(value))
        node.left = process()
        node.right = process()
        return node
    return process()




if __name__ == "__main__":
    numbers = [int(i.strip()) for i in input("Enter the numbers seperated by commas: ").split(",")]
    tree = Tree()
    for i in numbers:
        tree.addNode(tree.root, i)
    serializer = serialize(tree.root)
    new_serializer = serialize(deserialize(serializer))
    assert serializer == new_serializer


    
    
