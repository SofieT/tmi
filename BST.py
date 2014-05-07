__author__ = 'Ward Schodts en Robin Goots'


class Node(object):
    def __init__(self, info):  #constructor of class

        self.info = info  #information for node
        self.left = None  #left leef
        self.right = None  #right leef
        self.level = None  #level none defined

    def __str__(self):
        return str(self.info)  #return as string


class Searchtree(object):
    def __init__(self):  #constructor of class

        self.root = None

    def insert(self, point):  #create binary search tree nodes
        """
        Voeg een ount toe aan de BST
        """
        if self.root is None:

            self.root = Node(point)

        else:

            current = self.root

            while 1:

                status = point.compare(current.info)

                if status == 0:

                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(point)
                        break;

                elif status == 1:

                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(point)
                        break;

                elif status == 4:
                    # Punten komen overeen. Dit ondersteunen we niet.
                    break
                else:
                    break

    def pop(self):
        """
        Haal het dichtsbijzijnde punt uit de BST.
        """
        previous = None
        current = self.root
        while current is not None:
            if current.left is not None:
                previous = current
                current = current.left
            else:
                if previous is None:
                    self.root = current.right
                    return current.info
                else:
                    previous.left = current.right
                    return current.info

    def is_empty(self):
        return self.root is None