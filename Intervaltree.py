__author__ = 'Ward Schodts en Robin Goots'

class Node(object):

    left = None
    right = None

    def __init__(self, value, parent):  #constructor of class

        self.value = value #information for node
        self.parent = parent


class Intervaltree(object):

    root = None

    def insert(self, segment):

        if self.root is None:
            self.root is Node(segment, None)

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

    def deleteInterval(self, interval):

        node = self.search(interval)

        if node == self.root:
            self.root = None
            return
        #Geen kinderen
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        #Twee kinderen
        if node.left is not None and node.right is not None:
             node.left.parent = node.right
             node.right.parent = node.parent
             node.right.left = node.left
             if node == node.parent.left:
                 node.parent.left = node.right
             else:
                 node.parent.right = node.right
             node = None

        # 1 kind
        else:
            if node.left is not None:
                node.left.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                node.right.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
