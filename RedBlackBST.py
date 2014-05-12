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
        self.maxhi = val.hi



    def maxhi(self):
        if self.left is not None:
            a = self.left.segment.hi
        if self.right is not None:
            b = self.right.segment.hi
        c = self.key.segment.hi
        return max(a, b, c)

class RedBlackBST(object):

    root = None

    def maxhi(self):
        if self.left is not None:
            a = self.left.segment.hi
        if self.right is not None:
            b = self.right.segment.hi
        c = self.key.segment.hi
        return max(a, b, c)

    def isRed(self, node):
        if node is None:
            return False
        return node.color

    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = x.right.color
        x.right.color = True
        x.N = node.N
        node.N = self.size(node.left) + self.size(node.right) + 1
        self.maxhi()
        return x

    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = x.left.color
        x.left.color = True
        x.N = node.N
        self.maxhi()
        return x

    def flipColors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

        self.root.color = False

    def _put(self, node, key, val):

        if node is None:
            return Node(key, val, 1)

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

        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def delete(self, key):
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = True

        self.root = self._delete(self.root, key)

        if not self.isEmpty():
            self.root.color = False

    def _delete(self, node, key):
        if key.compare(node.key) == 0:
            if not self.isRed(node.left) and not self.isRed(node.left.left):
                node = self.moveRedLeft(node)
            node.left = self._delete(node.left, key)

        else:
            if self.isRed(node.left):
                node = self.rotateRight(node)
            if key.compare(node.key) == 2 and node.right is None:
                return None
            if not self.isRed(node.right) and not self.isRed(node.right.left):
                node = self.moveRedRight(node)
            if key.compare(node.key) == 2:
                x = self.min(node.right)
                node.key = x.key
                node.val = x.val
                node.right = self.deleteMin(node.right)
            else:
                node.right = self._delete(node.right, key)
        return self.balance(node)

    def min(self, node):
        if node.left is None:
            return node
        else:
            return self.min(node.left)


    def deleteMin(self, node):
        if node.left is None:
            return None

        if not self.isRed(node.left) and not self.isRed(node.left.left):
            node = self.moveRedLeft(node)

        node.left = self.deleteMin(node.left)
        return self.balance(node)

    def isEmpty(self):
        return self.root is None

    def size(self, node):
        if node is None:
            return 0
        return node.N
    def max(self, node):
        if node is None:
            return 0
        else:
            return node.maxhi

    def moveRedLeft(self, node):
        self.flipColors(node)
        if self.isRed(node.right.left):
            node.right = self.rotateRight(node.right)
            node = self.rotateLeft(node)
        return node

    def moveRedRight(self, node):
        self.flipColors(node)
        if self.isRed(node.left.left):
            node = self.rotateRight(node)
        return node

    def balance(self, node):
        if self.isRed(node.right):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def intervalSearch(self, segment, newroot):

        overlaplist = list()
        if segment.overlaps(newroot.val):
            overlaplist.append(segment)
            if newroot.left is not None:
                self.intervalSearch(segment, newroot.left.val)
            if newroot.left is not None:
                self.intervalSearch(segment, newroot.right.val)

        elif newroot.left.val is None and newroot.right is not None:
            self.intervalSearch(segment, newroot.right.val)

        else:
            self.intervalSearch(segment, newroot.left.val)