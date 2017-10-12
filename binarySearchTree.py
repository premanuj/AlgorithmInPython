class BinaryTree:
    tree = {}
    def __init__(self, rootid):
        self.rootid = rootid
        self.leftNode = None
        self.rightNode = None
    def getLeftNode(self, value):
        self.value = value
        return self.value
    def getRightNode(self, value):
        self.value = value
        return self.value
    def isEmpty(self, tree):
        self.tree = tree
        if self.tree:
            return False
        else:
            return True
    def isSmaller(self, parent, value):
        if parent > value:
            return True
        else:
            False
    def insertNode(self, value):
        self.value = value
        if isEmpty(self.tree):
            self.tree['node'] = {'value': self.rootid}
        elif isSmaller(self.rootid , self.value):
            self.tree[]


