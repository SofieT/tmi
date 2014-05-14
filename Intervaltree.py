__author__ = 'Ward Schodts en Robin Goots'

from queue import Queue

class Node(object):

    left = None
    right = None

    def __init__(self, value, parent):  #constructor of class

        self.value = value #information for node
        self.parent = parent
        self.maxhi = value.hi.yco


class Intervaltree(object):

    root = None

    def insert(self, segment):

        if self.root is None:
            self.root = Node(segment, None)


        else:

            current = self.root

            while True:

                status = segment.compare(current.value)

                if status == -1:

                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(segment, current)
                        break
                elif status == 1:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(segment, current)
                        break
                else:
                    raise NotImplemented
            self.updateMaxhi(current)


    def search(self, interval):

        current = self.root

        while True:
            status = interval.compare(current.value)

            if status == -1:
                current = current.left
            elif status == 1:
                current = current.right
            else:
                return current

    def searchOverlap(self, interval):

        intersectionList = list()
        nodeQueue = Queue()

        if self.root is None:
            return intersectionList

        nodeQueue.put(self.root)

        while not nodeQueue.empty():
            #node uit queue halen
            current = nodeQueue.get()
            if current.value.overlaps(interval):
                intersectionList.append(current.value.circle)

            if current.right is not None:
                nodeQueue.put(current.right)

            if current.left is not None:
                #nodeQueue.put(current.left)
                if  current.left.maxhi >= interval.lo.yco:
                    nodeQueue.put(current.left)


        return intersectionList

        # if root_node is None:
        #     root_node = self.root
        #
        # if interval.overlaps(root_node.value):
        #     intersectionList.append(root_node.value.circle)
        #
        #     if root_node.left is not None:
        #         current = root_node.left
        #         self.searchOverlap(interval, current)
        #     if root_node.right is not None:
        #         current = root_node.right
        #         self.searchOverlap(interval, current)
        #
        # elif root_node.left is None and root_node.right is not None:
        #     self.searchOverlap(interval, root_node.right)
        #
        # elif root_node.left is not None and root_node.left.value.maxhi < interval.lo.yco:
        #     root_node.left = None
        #     current = root_node.right
        #     self.searchOverlap(interval, current)
        #
        # elif root_node.left is not None:
        #     current = root_node.left
        #     self.searchOverlap(interval, current)
        # else:
        #     return intersectionList


    def deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin(node.left)

        return node

    def size(self, x):
        if x is None:
            return 0
        else:
            return x.maxhi

    def findMin(self, node):
        if node.right is None:
            return node
        minimum = node.right

        while True:

            if minimum.left is not None:
                minimum = minimum.left
            else:
                return minimum




    def delete(self, key):
        minimumnode = self.search(key)

        if self.findMin(minimumnode).parent is not None:
            nodetoupdate = self.findMin(minimumnode).parent
        else:
            nodetoupdate = self.findMin(minimumnode)
        self.root = self._delete(self.root, key)
        self.updateMaxhi(nodetoupdate)

    def _delete(self, x, value):
        if x is None:
            return None
        cmp = value.compare(x.value)
        if cmp < 0:
            x.left = self._delete(x.left, value)
        elif cmp > 0:
            x.right = self._delete(x.right, value)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self.deleteMin(t.right)
            x.left = t.left
        return x

    def _min(self, x):
        if x.left is None:
            return x
        else:
            return self._min(x.left)

    def updateMaxhi(self, node):
        while node is not None:
            a = b = 0
            if node.left is not None:
                a = node.left.maxhi
            if node.right is not None:
                b = node.right.maxhi
            node.maxhi = max(node.value.hi.yco, a, b)

            node = node.parent