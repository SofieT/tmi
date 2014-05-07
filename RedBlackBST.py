__author__ = 'warreee'


class Node(object):
    """
    RED = true
    BLACK = false
    """
    def __init__(self, key, val, color = False, N = 0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.N = N # number of nodes in this subtree
        self.color = color

        self.max = 0

class RedBlackBST(object):
    def isRed(self, node):
        if node is None:
            return False
        return node.color

    def rotateRight(self, node):
        node_x = node.left
        node.left = node_x.right
        node_x.right = node
        node_x.color = node.color
        node.color = True
        node_x.N = node.N
        node.N = node.left.N + node.right.N + 1
        #max voor node
        node.max = max(node.max, node.left.max, node.right.max)
        #max voor node_x
        node_x.max = max(node_x.max, node_x.left.max, node_x.right.max)
        return node_x

    def rotateLeft(self, node):
        node_x = node.right
        node.right = node_x.left
        node_x.left = node
        node_x.color = node.color
        node.color = True
        node_x.N = node.N
        node.N = node.left.N + node.right.N + 1
        #max voor node
        node.max = max(node.max, node.left.max, node.right.max)
        #max voor node_x
        node_x.max = max(node_x.max, node_x.left.max, node_x.right.max)
        return node_x

    def flipColors(self, node):
        node.color = True
        node.left.color = False
        node.right.color = False

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

        self.root.color = False

    def _put(self, node, key, val):

        if node is None:
            return Node(key, True, 1)

        cmp = key.compare(node.key)
        if cmp == 0:
            node.left = self._put(node.left, key, val)
        elif cmp == 1:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        node.N = node.left.N + node.right.N + 1
        return node