__author__ = 'Ward Schodts en Robin Goots'

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

    def searchOverlap(self, interval, root_node = None):

        intersectionList = list()

        if root_node is None:
            root_node = self.root

        if interval.overlaps(root_node.value):
            intersectionList.append(root_node.value.circle)

            if root_node.left is not None:
                current = root_node.left
                self.searchOverlap(interval, current)
            if root_node.right is not None:
                current = root_node.right
                self.searchOverlap(interval, current)

        elif root_node.left is None and root_node.right is not None:
            self.searchOverlap(interval, root_node.right)

        elif root_node.left is not None and root_node.left.value.maxhi < interval.lo.yco:
            root_node.left = None
            current = root_node.right
            self.searchOverlap(interval, current)

        elif root_node.left is not None:
            current = root_node.left
            self.searchOverlap(interval, current)
        else:
            return intersectionList



    def deleteRoot(self):
        root = self.root
        if root.left is None and root.right is None:
            self.root = None

        elif root.left is not None and root.right is not None:
            minimum = self.findMin(root)

            minimum.left = root.left
            if minimum.right is None:
                minimum.right = root.right
            else:
                minimum.parent.right = minimum.right
                minimum.right = root.right
            #TODO implementeren
            self.root = minimum

        else:
            if root.left is not None:
                self.root = root.left
                self.root.parent = None
            else:
                self.root = root.right
                self.root.parent = None



    def findMin(self, node):
        minimum = node.right
        while True:
            if minimum.left is not None:
                minimum = minimum.left
            else:
                break

        return minimum

    def deleteInterval(self, interval):

        node = self.search(interval)

        if node == self.root:

            self.deleteRoot()
            return

        #Geen kinderen
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            self.updateMaxhi(node.parent)

        #Twee kinderen
        elif node.left is not None and node.right is not None:

            # zoek min in rechter subtree.
            minimum = self.findMin(node)# node.left.parent = minimum
            # minimum.parent = node.parent
            # minimum.left = node.left
            #
            # if node.right != minimum:
            #     minimum.right = node.right
            # node = minimum

            #parent = node.parent
            minimum_right = minimum.right

            minimum.left = node.left
            if not minimum == node.right:
                minimum.right = node.right

            if minimum_right is not None:
                minimum.parent.left = minimum_right
                minimum_right = minimum.parent
                minimum.right = None
                #TODO correctheid verefiëren
            else:
                minimum.parent.left = None

            minimum.parent = node.parent
            if node.parent.left == node:
                node.parent.left = minimum
            else:
                node.parent.right = minimum

            # min kan nog rechterkind bevatten of geen meer



            self.updateMaxhi(node.right)

        # 1 kind
        else:
            if node.left is not None:
                node.left.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                self.updateMaxhi(node.left)
            else:
                node.right.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                self.updateMaxhi(node.right)
    def deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin(node.left)
        node.maxhi = self.size(node.left)
        return node

    def size(self, x):
        if x is None:
            return 0
        else:
            return x.maxhi
    def delete(self, key):
        self.root = self._delete(self.root, key)

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
            return min(x.left   )
    def updateMaxhi(self, node):
        while node is not self.root:
            a = b = 0
            if node.left is not None:
                a = node.left.maxhi
            if node.right is not None:
                b = node.right.maxhi
            node.maxhi = max(node.value.hi.yco, a, b)

            node = node.parent